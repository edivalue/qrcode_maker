import qrcode

def generate_qrcode(text_input, pic_file):
#class QRCode(version=None, error_correction=constants.ERROR_CORRECT_M, box_size=10, border=4, image_factory=None, mask_pattern=None)    
    qrcodes = qrcode.QRCode(version = 1 ,
    error_correction = qrcode.constants.ERROR_CORRECT_H ,
    box_size = 11 ,
    border = 4 ,
    image_factory = None ,
    mask_pattern= 1 )
    
    qrcodes.add_data(text_input)
    qrcodes.make(fit=True)#ff23ff
    
    img = qrcodes.make_image(fill_color = '#AA0000', background_color = "#7aff9b")
    img.save(pic_file)

text_input = input('Enter the text you converted to a QR Code >>> ')
pic_file = './QrCodePicture.png'
generate_qrcode(text_input, pic_file)
    