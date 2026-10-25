"""Retoque localizado da foto alinhada: remove remendos residuais (inpaint pequeno + grão). Uso: retocar_alinhada.py ENTRADA SAIDA"""
import sys, cv2, numpy as np
ent, sai = sys.argv[1], sys.argv[2]
im = cv2.imread(ent); H, W = im.shape[:2]
# (x0,y0,x1,y1) em coordenadas da imagem, elipses de retoque
REG = [(487,500,512,522),   # remendo claro sob a borda da copa
       (563,510,580,545),   # cunha escura junto à haste
       (772,178,806,208)]   # lasca clara na parede, canto da copa
m = np.zeros((H, W), np.uint8)
for x0,y0,x1,y1 in REG:
    cv2.ellipse(m, ((x0+x1)//2,(y0+y1)//2), ((x1-x0)//2,(y1-y0)//2), 0, 0, 360, 255, -1)
out = cv2.inpaint(im, m, 6, cv2.INPAINT_TELEA)
rng = np.random.default_rng(7)
g = rng.normal(0, 2.2, im.shape).astype(np.float32)
mm = (cv2.GaussianBlur(m, (0,0), 2).astype(np.float32)/255)[..., None]
res = np.clip(out.astype(np.float32) + g*mm, 0, 255).astype(np.uint8)
# mistura suave nas bordas
res = (im*(1-mm) + res*mm).astype(np.uint8)
# 2) cópia de parede limpa sobre o remendo claro e a cunha escura (fonte deslocada, borda suave)
def cobrir(res, box, dx, dy, sig=2.5):
    x0,y0,x1,y1 = box
    mk = np.zeros((H, W), np.float32); cv2.rectangle(mk, (x0,y0), (x1,y1), 1.0, -1)
    mk = cv2.GaussianBlur(mk, (0,0), sig)[..., None]
    src = np.roll(np.roll(res, dy, axis=0), dx, axis=1)   # src[y,x] = res[y-dy, x-dx]
    return (res*(1-mk) + src*mk).astype(np.uint8)
res = cobrir(res, (484,500,514,524), 0, -28)       # patch claro: usa parede abaixo
res = cobrir(res, (560,512,573,548), 22, 0)      # cunha escura: usa parede à esquerda
cv2.imwrite(sai, res)
