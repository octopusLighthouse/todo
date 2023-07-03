import qrcode
import io

from flask import Flask, redirect, render_template, url_for, make_response, Response

app = Flask(__name__)
@app.get('/qr')
#@app.route('/qr', methods=['GET'])
def generate_qr():
    # Generate QR code for an external URL
    target_url = "https://discogs.com"

    # Generate QR code
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(target_url)
    qr.make(fit=True)

    # Create an image from the QR code
    qr_image = qr.make_image(fill_color='black', back_color='white')

    # Create a response object
    response = make_response()
    response.data = qr_image.get_image().tobytes()
    response.headers['Content-Type'] = 'image/png'

    return response

if __name__ == '__main__':
    app.run()
if __name__ == '__main__':
    app.run()