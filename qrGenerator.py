import qrcode


class QrCode:
    def __init__(self,size:int,padding:int):
        self.qr =qrcode.QRCode(box_size=size,border=padding)
    def createQrcode(self,filename:str,fg:str,bg:str):
        user:str = input("Enter the code to qrcode")
        try:
            self.qr.add_data(user)
            qr_image = self.qr.make_image(fill_color=fg,back_colot=bg)
            qr_image.save(filename)
            print(f"Successfull {filename}")
        except Exception as e:
            print(f"error {e}")

def main():
    qrCode = QrCode(size=30,padding=2)
    qrCode.createQrcode("qr.png",fg="black",bg="white")

if __name__ == '__main__':
    main()