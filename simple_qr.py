import qrcode as qr 
img=qr.make("https://www.youtube.com/")
img.save("c:\Users\manas\OneDrive\Desktop\coding\.vscode\python\simple_qryoutubeQR.png")

#this code directly creates a QR code without any customizaton.It has white background with the QR being in black.