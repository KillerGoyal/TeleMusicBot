HEROKU = True   # NOTE Make it false if you're not deploying on heroku.

# NOTE these values are for heroku.
if HEROKU:
    from os import environ
    API_ID = int(environ["API_ID"])
    API_HASH = environ["API_HASH"]
    SUDO_CHAT_ID = environ["SUDO_CHAT_ID"]
    SESSION_STRING = environ["SESSION_STRING"]

# NOTE Fill this if you are not deploying on heroku.
if not HEROKU:
    API_ID = 123456
    API_HASH = "asdnsfkj1412kjh4"
    SUDO_CHAT_ID = "12304"


# don't make changes below this line
ARQ_API = "http://35.240.133.234:8000"
KEY = "VNDYQL-MORNWL-UAIETE-KYJFWX-ARQ"
SESSION = "AQAScrqJQnA90grgO_9SpMTyVoOjyiVAFarAdFquJZ4959RRJna3PTx3P2IhpNO4E6OAAdBRvnX7tVXV319pLwDnFx_xDl6RtaB8WSO5x16vlBtKzwTT1V5jTCxKJ4O6Pg5oosKwJqIkG3b3aAUh-Hd9ozw925b5DHR8IYuKeZbfi1YXYga_HPvp4gKLAb6Ug_XeGzR9na9u0NZEQ2pnZHKG4a6qpg-QDNAyI7iOoFuM9-uRZcYmGHmiHxQ-2OhpnbsJy0SNVj_FhKLpgMx05hBaiMCFE4T1OPDF05GpLxkm39OH_mOjrZu7BCNlV6-w8t3s4jN4uZ6J3jwyAXAzL1Y7ay_B4gA"
