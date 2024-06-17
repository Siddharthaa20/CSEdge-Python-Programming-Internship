Delivered-To: siddharthaarepalli46@gmail.com
Received: by 2002:a59:552:0:b0:463:f90a:5760 with SMTP id 79csp1802205vqf;
        Mon, 17 Jun 2024 04:13:35 -0700 (PDT)
X-Received: by 2002:adf:f305:0:b0:35f:650:e915 with SMTP id ffacd0b85a97d-3607a7d97bdmr6136815f8f.53.1718622815199;
        Mon, 17 Jun 2024 04:13:35 -0700 (PDT)
ARC-Seal: i=1; a=rsa-sha256; t=1718622815; cv=none;
        d=google.com; s=arc-20160816;
        b=aaEZyJ0F8Gt8BEJHNWigXvmlPXDPqGTycHqQ8moF32k+DdksfK5VPEKMXwE6Z9GtdV
         uD0UYs57T6zFd/Cc9tXqHs9EcfqUY+Q1YjDNviHwhqiVDpaeEB3UI96bE1Hj0lrrhKYA
         yPasB6M5vdkNvlKKR1psOfWXSd5m7nIRcrIsozRyvniuIC9yyi+oduz9+D3dasDQtJ59
         dWOTnDmXJEMG6LaX7T9BF5ApdVfG0jc3Z3c5a62877bvFssGFY7HngbDzpvF71ajZQTh
         J8PNP/cNMLQ/bkpVpBaBr7JrAju0aWbKV36JcAyzYElK3Vp9GmPRKLeN7yrFiJyA7+y0
         UqEA==
ARC-Message-Signature: i=1; a=rsa-sha256; c=relaxed/relaxed; d=google.com; s=arc-20160816;
        h=to:subject:message-id:date:from:mime-version:dkim-signature;
        bh=0MrjvYh0JwDOUORdnWmzzFJP71Av52Vi+16/gZccnE8=;
        fh=ogtUl7XzfsmBwMTFbUaql7G2PHzPz+ca7PDOvyDOPpk=;
        b=ZrHsno8D75xSFlvr1C8QXUyZDLj5Whr911hkriSNHR+PlEm70bF53/tuckUoLk3oKW
         OVaUwBdAZDyTGDwdi/muu/AY4cHZYteyQARGWvVh87ukc16g3lgjvJETihf7HkLsjC2d
         PMb6XgzEZI193C+7OAbH/gaEbaMVVbZDwPidT8m7yatoaFEo7A1jSjsMQ6LivoOMZX96
         dHUSs6+JuPIMYpN95Ulol93RRZNq4Oh24hkiQVUWQle3MRj9QMxVqInRU8Gwq1R0mrFB
         BbliXNc+6qI00c2LNRSKbf5BDCiJo0jCDjYZOa7v2E10WcmIvlZ1z6W/UmvRLB0r6PYf
         Wqdw==;
        dara=google.com
ARC-Authentication-Results: i=1; mx.google.com;
       dkim=pass header.i=@gmail.com header.s=20230601 header.b=QrELRCSa;
       spf=pass (google.com: domain of meghanakankati24@gmail.com designates 209.85.220.41 as permitted sender) smtp.mailfrom=meghanakankati24@gmail.com;
       dmarc=pass (p=NONE sp=QUARANTINE dis=NONE) header.from=gmail.com
Return-Path: <meghanakankati24@gmail.com>
Received: from mail-sor-f41.google.com (mail-sor-f41.google.com. [209.85.220.41])
        by mx.google.com with SMTPS id ffacd0b85a97d-36083d6e5c1sor1775994f8f.0.2024.06.17.04.13.35
        for <siddharthaarepalli46@gmail.com>
        (Google Transport Security);
        Mon, 17 Jun 2024 04:13:35 -0700 (PDT)
Received-SPF: pass (google.com: domain of meghanakankati24@gmail.com designates 209.85.220.41 as permitted sender) client-ip=209.85.220.41;
Authentication-Results: mx.google.com;
       dkim=pass header.i=@gmail.com header.s=20230601 header.b=QrELRCSa;
       spf=pass (google.com: domain of meghanakankati24@gmail.com designates 209.85.220.41 as permitted sender) smtp.mailfrom=meghanakankati24@gmail.com;
       dmarc=pass (p=NONE sp=QUARANTINE dis=NONE) header.from=gmail.com
DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/relaxed;
        d=gmail.com; s=20230601; t=1718622814; x=1719227614; dara=google.com;
        h=to:subject:message-id:date:from:mime-version:from:to:cc:subject
         :date:message-id:reply-to;
        bh=0MrjvYh0JwDOUORdnWmzzFJP71Av52Vi+16/gZccnE8=;
        b=QrELRCSaiScITidMe3gtm4Z4olpvoJIrilh16LqaHNqcGXse8wRfwMDed7N0+fL79Y
         fsnbrxdjOhOIEzAdfZbiFBDRKXBCuC6LwwnpVTWnj7Va4OHjnWR4i73LTrL5MVNc9KGq
         Jnddsr6dXGfA4LdIvZsTbeyFse0w/QVNTQLRBYGfso8Sj230yYsmr1IXVwNE/oYMc2/F
         1A7lXQminQ3jQ9RM7gsA61wup7jll/5apUm3K2PwZvqsj+z7eF08KlBbEcQTAehf4LNW
         Ym17PO9r8/YHSWrFvTCf2jzRH+1AXsImumpMU2jy9BkoWxvnm6U1houPevxWPZuaSaOe
         fcjg==
X-Google-DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/relaxed;
        d=1e100.net; s=20230601; t=1718622814; x=1719227614;
        h=to:subject:message-id:date:from:mime-version:x-gm-message-state
         :from:to:cc:subject:date:message-id:reply-to;
        bh=0MrjvYh0JwDOUORdnWmzzFJP71Av52Vi+16/gZccnE8=;
        b=N0sIZtyz8Ntp59x+IVUsBNYnaw8iyYHwb7+Q7nGEE1koYDGrvrrf+U4F/7jbZteEDP
         Orvh1V8OITz/AHdSoDWsGBYOJqXsQ16d8DUQoHzUk9PXHlJmCoTNm74UjYWyYNDlbaQm
         F1A9/DgF0fKtpAsMy0/NgaiBH9CzC8JM8xJckMmzEaTU22s6PvGJGIv544CMLkMn1jJf
         rKNAguL1IxI+4PGOjY662stRr4YM443wTwRTQeS/P+lJrZhxjhvWwnL02/M5mFp3MqW/
         gn4RQooa29jeZ2i86FYcP5kgsnQSQSN7OuWNp4cMh6MbGUTVrMsQuF3r/HUcXhiupaA1
         IO7w==
X-Gm-Message-State: AOJu0Yzsia6S32KIKUJYGOketJihKdKowln1SxBYSiu2TucgDg446v+r
	BmW7UpjooLKJRwlM30oo2+mlejR35kqwy7rb55FO66hkcctA7sV1Ha9zYt9uBd43iIPsssswdEj
	T4SNOAKeSoydU2FECRhWHhapvBmGmmLBv
X-Google-Smtp-Source: AGHT+IFnGFxSGBiutojDoAuNkTChT2WIVmSbJ0ezXWx8EXaPEDlmWd+icVuUQj9fYabor6dUliYTEu1wRGd/PGjqJ7U=
X-Received: by 2002:a5d:618d:0:b0:360:9180:760f with SMTP id
 ffacd0b85a97d-3609180775fmr2486187f8f.66.1718622814258; Mon, 17 Jun 2024
 04:13:34 -0700 (PDT)
MIME-Version: 1.0
From: Meghana _k <meghanakankati24@gmail.com>
Date: Mon, 17 Jun 2024 16:43:21 +0530
Message-ID: <CAB1d5xJ7e6N+ANXV5vPK_Q8KPch=-ES0KzZO++z3DzhSmLTnQA@mail.gmail.com>
Subject: task1
To: AREPALLI SIDDHARTHA <siddharthaarepalli46@gmail.com>
Content-Type: multipart/alternative; boundary="00000000000058d06d061b140eeb"

--00000000000058d06d061b140eeb
Content-Type: text/plain; charset="UTF-8"
Content-Transfer-Encoding: quoted-printable

import requests

def get_weather_data(api_key, city_name):
    url =3D f"
http://api.openweathermap.org/data/2.5/weather?q=3D{city_name}&appid=3D{api=
_key}&units=3Dmetric
"
    response =3D requests.get(url)
    data =3D response.json()
    return data

def display_current_weather(data):
    print("Current Weather Conditions:")
    print("---------------------------")
    print(f"Weather: {data['weather'][0]['description']}")
    print(f"Temperature: {data['main']['temp']}=C2=B0C")
    print(f"Humidity: {data['main']['humidity']}%")
    print(f"Wind Speed: {data['wind']['speed']} m/s")

def get_forecast(api_key, city_name):
    url =3D f"
http://api.openweathermap.org/data/2.5/forecast?q=3D{city_name}&appid=3D{ap=
i_key}&units=3Dmetric
"
    response =3D requests.get(url)
    data =3D response.json()
    return data

def display_forecast(data):
    print("\nWeather Forecast for the next 5 days:")
    print("-------------------------------------")
    for forecast in data['list']:
        print(f"Date: {forecast['dt_txt']}")
        print(f"Weather: {forecast['weather'][0]['description']}")
        print(f"Temperature: {forecast['main']['temp']}=C2=B0C")
        print("")

def main():
    api_key =3D 'b73f861c9b47fe465e680a5d330e01eb'
    city_name =3D input("Enter city name: ")

    current_weather_data =3D get_weather_data(api_key, city_name)
    display_current_weather(current_weather_data)

    forecast_data =3D get_forecast(api_key, city_name)
    display_forecast(forecast_data)

if __name__ =3D=3D "__main__":
    main()

--00000000000058d06d061b140eeb
Content-Type: text/html; charset="UTF-8"
Content-Transfer-Encoding: quoted-printable

<div dir=3D"ltr">import requests<br><br>def get_weather_data(api_key, city_=
name):<br>=C2=A0 =C2=A0 url =3D f&quot;<a href=3D"http://api.openweathermap=
.org/data/2.5/weather?q=3D{city_name}&amp;appid=3D{api_key}&amp;units=3Dmet=
ric">http://api.openweathermap.org/data/2.5/weather?q=3D{city_name}&amp;app=
id=3D{api_key}&amp;units=3Dmetric</a>&quot;<br>=C2=A0 =C2=A0 response =3D r=
equests.get(url)<br>=C2=A0 =C2=A0 data =3D response.json()<br>=C2=A0 =C2=A0=
 return data<br><br>def display_current_weather(data):<br>=C2=A0 =C2=A0 pri=
nt(&quot;Current Weather Conditions:&quot;)<br>=C2=A0 =C2=A0 print(&quot;--=
-------------------------&quot;)<br>=C2=A0 =C2=A0 print(f&quot;Weather: {da=
ta[&#39;weather&#39;][0][&#39;description&#39;]}&quot;)<br>=C2=A0 =C2=A0 pr=
int(f&quot;Temperature: {data[&#39;main&#39;][&#39;temp&#39;]}=C2=B0C&quot;=
)<br>=C2=A0 =C2=A0 print(f&quot;Humidity: {data[&#39;main&#39;][&#39;humidi=
ty&#39;]}%&quot;)<br>=C2=A0 =C2=A0 print(f&quot;Wind Speed: {data[&#39;wind=
&#39;][&#39;speed&#39;]} m/s&quot;)<br><br>def get_forecast(api_key, city_n=
ame):<br>=C2=A0 =C2=A0 url =3D f&quot;<a href=3D"http://api.openweathermap.=
org/data/2.5/forecast?q=3D{city_name}&amp;appid=3D{api_key}&amp;units=3Dmet=
ric">http://api.openweathermap.org/data/2.5/forecast?q=3D{city_name}&amp;ap=
pid=3D{api_key}&amp;units=3Dmetric</a>&quot;<br>=C2=A0 =C2=A0 response =3D =
requests.get(url)<br>=C2=A0 =C2=A0 data =3D response.json()<br>=C2=A0 =C2=
=A0 return data<br><br>def display_forecast(data):<br>=C2=A0 =C2=A0 print(&=
quot;\nWeather Forecast for the next 5 days:&quot;)<br>=C2=A0 =C2=A0 print(=
&quot;-------------------------------------&quot;)<br>=C2=A0 =C2=A0 for for=
ecast in data[&#39;list&#39;]:<br>=C2=A0 =C2=A0 =C2=A0 =C2=A0 print(f&quot;=
Date: {forecast[&#39;dt_txt&#39;]}&quot;)<br>=C2=A0 =C2=A0 =C2=A0 =C2=A0 pr=
int(f&quot;Weather: {forecast[&#39;weather&#39;][0][&#39;description&#39;]}=
&quot;)<br>=C2=A0 =C2=A0 =C2=A0 =C2=A0 print(f&quot;Temperature: {forecast[=
&#39;main&#39;][&#39;temp&#39;]}=C2=B0C&quot;)<br>=C2=A0 =C2=A0 =C2=A0 =C2=
=A0 print(&quot;&quot;)<br><br>def main():<br>=C2=A0 =C2=A0 api_key =3D &#3=
9;b73f861c9b47fe465e680a5d330e01eb&#39; <br>=C2=A0 =C2=A0 city_name =3D inp=
ut(&quot;Enter city name: &quot;)<br>=C2=A0 =C2=A0 <br>=C2=A0 =C2=A0 curren=
t_weather_data =3D get_weather_data(api_key, city_name)<br>=C2=A0 =C2=A0 di=
splay_current_weather(current_weather_data)<br>=C2=A0 =C2=A0 <br>=C2=A0 =C2=
=A0 forecast_data =3D get_forecast(api_key, city_name)<br>=C2=A0 =C2=A0 dis=
play_forecast(forecast_data)<br><br>if __name__ =3D=3D &quot;__main__&quot;=
:<br>=C2=A0 =C2=A0 main()<br></div>

--00000000000058d06d061b140eeb--
