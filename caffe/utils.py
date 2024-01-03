from kavenegar import *

def send_otp_code(mobile_phone, code):
    try:
        api = KavenegarAPI('Your APIKey', timeout=120)
        params = {
            'sender': '',#optional
            'receptor': mobile_phone,
            'message': f'کد تایید شمار {code} است',
        } 
        response = api.sms_send(params)
        print(response)
    except APIException as e:
        print(e)
    except HTTPException as e:
        print(e)