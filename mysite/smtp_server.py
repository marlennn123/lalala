# smtp_server.py
from aiosmtpd.controller import Controller
import asyncio

class MyHandler:
    async def handle_DATA(self, server, session, envelope):
        print(f"Received message from: {envelope.mail_from}")
        print(f"Message addressed to: {envelope.rcpt_tos}")
        print("Message data:")
        print(envelope.content.decode('utf-8'))

async def main():
    controller = Controller(MyHandler(), hostname='localhost', port=3000)  # изменение порта на 3000
    controller.start()
    await asyncio.sleep(3600)

if __name__ == '__main__':
    asyncio.run(main())
