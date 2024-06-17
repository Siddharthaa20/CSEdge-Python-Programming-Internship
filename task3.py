Delivered-To: siddharthaarepalli46@gmail.com
Received: by 2002:a59:552:0:b0:463:f90a:5760 with SMTP id 79csp1802463vqf;
        Mon, 17 Jun 2024 04:14:13 -0700 (PDT)
X-Received: by 2002:a2e:7a18:0:b0:2ea:83b5:40cf with SMTP id 38308e7fff4ca-2ec0e5b533cmr59480671fa.3.1718622853748;
        Mon, 17 Jun 2024 04:14:13 -0700 (PDT)
ARC-Seal: i=1; a=rsa-sha256; t=1718622853; cv=none;
        d=google.com; s=arc-20160816;
        b=Eya2iRJUtaBIHJo/DxfYb6oqZSlZi7GRHnzsbcudQ0SasPjJNj7jpEvo3ihPjwi7st
         ISa4Oj8mSO134uU81N+C/ZGGwnm6cFsLuoarMqRhYM2p8IEcAlYk9H/t+75in8sZtP9l
         e4dYLMLrIgmkDiU0y3Tw2e/6Qv/IC/LMnjDT5n/7NtrM8wlIA2qkMO+ms4rTfDYAw/lo
         2G1WLGib18AueRtNfQgjGgwVmV7ERBJ+I0KHgEDtFWctu9/PzKIg45zmvVahsL292tso
         DYoS+kE7zskQefcikLG3HWXIdJpD+sIVqrabB6UGCFP5HbBnO6atwXwSeFTt199rUtq4
         oZ5Q==
ARC-Message-Signature: i=1; a=rsa-sha256; c=relaxed/relaxed; d=google.com; s=arc-20160816;
        h=to:subject:message-id:date:from:mime-version:dkim-signature;
        bh=CTomWYM64SnRzs7Lh+alAtA9ap0uu8NCRP1fPLaFXus=;
        fh=ogtUl7XzfsmBwMTFbUaql7G2PHzPz+ca7PDOvyDOPpk=;
        b=j9iEaTx6uPqlKSNaaGmTKUd2ZjGVpOREBiqYSIqt7ajmvum3ndZrABn3QcAkUZGBl+
         CeRx5uaurnrog+b6BmcOedRWI9uJCOrGambGwWAnuw/wIUEvxY4X++LyaPdJsXoCw/JO
         D8u49QSP8zYB2z+7q2SiVoMdlgATNCOuZEcuPQgSuLbOR6yYa0HUJBaiXTECYrRS7+1u
         hkyAd0tvZhiPHhyromhJbhvkXOReICoGWC4rfzC/MpwCuLekAVP+skomv2wecxCXjmac
         6UgjFg6VHQMaXRadopHFCI5LcLoqbhzkiyEQbxZnbxREQeaHm/Wne2KkIO1cDJCF2bOr
         MDWQ==;
        dara=google.com
ARC-Authentication-Results: i=1; mx.google.com;
       dkim=pass header.i=@gmail.com header.s=20230601 header.b=VJpunn9i;
       spf=pass (google.com: domain of meghanakankati24@gmail.com designates 209.85.220.41 as permitted sender) smtp.mailfrom=meghanakankati24@gmail.com;
       dmarc=pass (p=NONE sp=QUARANTINE dis=NONE) header.from=gmail.com
Return-Path: <meghanakankati24@gmail.com>
Received: from mail-sor-f41.google.com (mail-sor-f41.google.com. [209.85.220.41])
        by mx.google.com with SMTPS id 38308e7fff4ca-2ec05cb94d3sor23061581fa.14.2024.06.17.04.14.13
        for <siddharthaarepalli46@gmail.com>
        (Google Transport Security);
        Mon, 17 Jun 2024 04:14:13 -0700 (PDT)
Received-SPF: pass (google.com: domain of meghanakankati24@gmail.com designates 209.85.220.41 as permitted sender) client-ip=209.85.220.41;
Authentication-Results: mx.google.com;
       dkim=pass header.i=@gmail.com header.s=20230601 header.b=VJpunn9i;
       spf=pass (google.com: domain of meghanakankati24@gmail.com designates 209.85.220.41 as permitted sender) smtp.mailfrom=meghanakankati24@gmail.com;
       dmarc=pass (p=NONE sp=QUARANTINE dis=NONE) header.from=gmail.com
DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/relaxed;
        d=gmail.com; s=20230601; t=1718622853; x=1719227653; dara=google.com;
        h=to:subject:message-id:date:from:mime-version:from:to:cc:subject
         :date:message-id:reply-to;
        bh=CTomWYM64SnRzs7Lh+alAtA9ap0uu8NCRP1fPLaFXus=;
        b=VJpunn9iuWdB1GDxqF6updCoJcy29/YQUtDmieIoFfBqdEoywITv+iXE1O7p1Lelyw
         WR7BfXff3JTchSu1e3CV4eEOvwAx+yVJLFRuchAl/lp24NEZmXyQ4skuz8Zsp/CgI9yz
         lG00+Wq6zNWrIM5B8tzj5NsBB0k1oBji7DrjFkfvRyjBmzRh8rMs2BgGKLUWmfyFs5e7
         6sTfOhUGQBAWpBAMrDXRHOtJWgyGeTiPozuVsTiHPK8ZtQ7RtS3T01sVeDieWv7F9JLS
         VVuaW6imxVOx6R4V1RWbAgkIWy5B/sb3LMhaAdHcFW+ohOUwfu4Vscky+/BL2CHS/56J
         DHPg==
X-Google-DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/relaxed;
        d=1e100.net; s=20230601; t=1718622853; x=1719227653;
        h=to:subject:message-id:date:from:mime-version:x-gm-message-state
         :from:to:cc:subject:date:message-id:reply-to;
        bh=CTomWYM64SnRzs7Lh+alAtA9ap0uu8NCRP1fPLaFXus=;
        b=vUw4iRQfM7r7Tm/X7ZGZ5nSg9Zmez/3ZR11/EfDRY6CInHAgSQJV3qq0O6ujMRY61w
         MbUXhZnErtvwx8KdoYrS7badXpj+ps4Ukbva9JZ8Mgj9p/qP9Hno8kUqzjBKxLth1Zcx
         cK6+dsiK2CXx19S31uW4DvToD93UjW7CF0PzDT9vGFbiuUOEnG9/E4H9nKidB2kJOKTC
         yqpT/XPVGIuiMAYUYWsfL8enkKqsZdJPKsMJIeWFS//pMJniSAikX31GVlIFd8rE9NWX
         8QufNb3/8oLiKl/OBrhSPNs8x02VtBvoD13gIrHf6yRdE8BiSKhVTkBIesHKKCgGRxt+
         s2HA==
X-Gm-Message-State: AOJu0YyT+1QPlnOsjELKHidr4E+M6yBlePh7ZAkWx9uKj+FH4NlUbaEH
	cdehJcLSbNviU4gvYukVaqvJnwyHrbnvGJMr/Ir8fRV53oL6mz+Xmh9jXdF86Y5lo/Nru/1qFCE
	yrLD7AaLPOtKaXBnVPJ1eh0WumhTTLgv4
X-Google-Smtp-Source: AGHT+IHfVFUsO3gp56ITRAg28jLZs9BjAp9xnxFTM28jYsYgUHzJbBPCWHgZLpF3eMkmqAzzr9RkIMp639Wa4wswcPc=
X-Received: by 2002:a2e:97d1:0:b0:2ec:1dfa:5155 with SMTP id
 38308e7fff4ca-2ec1dfa57f9mr42458941fa.32.1718622852765; Mon, 17 Jun 2024
 04:14:12 -0700 (PDT)
MIME-Version: 1.0
From: Meghana _k <meghanakankati24@gmail.com>
Date: Mon, 17 Jun 2024 16:44:01 +0530
Message-ID: <CAB1d5xLpsL7p1HYc_HbKk7tED_B=42xrHZbqyA+4P9UnRDmMEA@mail.gmail.com>
Subject: task3
To: AREPALLI SIDDHARTHA <siddharthaarepalli46@gmail.com>
Content-Type: multipart/alternative; boundary="000000000000a4633d061b14109c"

--000000000000a4633d061b14109c
Content-Type: text/plain; charset="UTF-8"

import nltk
from nltk.chat.util import Chat, reflections

# Define patterns and responses
patterns = [
    (r'hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']),
    (r'how are you?', ["I'm doing well, thank you!", "I'm great, thanks for
asking!"]),
    (r'what is your name?', ["I'm just a simple chatbot.", "I'm a chatbot
designed to assist you."]),
    (r'bye|goodbye', ["Goodbye!", "See you later!", "Bye!"]),
    # Add more patterns and responses as needed
]

# Create a chatbot
chatbot = Chat(patterns, reflections)

# Define a function to chat with the user
def chat():
    print("Hello! How can I assist you today?")
    while True:
        user_input = input("> ")
        response = chatbot.respond(user_input)
        print(response)
        if user_input.lower() == 'bye':
            break

# Start the chat
if __name__ == "__main__":
    chat()

--000000000000a4633d061b14109c
Content-Type: text/html; charset="UTF-8"
Content-Transfer-Encoding: quoted-printable

<div dir=3D"ltr">import nltk<br>from nltk.chat.util import Chat, reflection=
s<br><br># Define patterns and responses<br>patterns =3D [<br>=C2=A0 =C2=A0=
 (r&#39;hi|hello|hey&#39;, [&#39;Hello!&#39;, &#39;Hi there!&#39;, &#39;Hey=
!&#39;]),<br>=C2=A0 =C2=A0 (r&#39;how are you?&#39;, [&quot;I&#39;m doing w=
ell, thank you!&quot;, &quot;I&#39;m great, thanks for asking!&quot;]),<br>=
=C2=A0 =C2=A0 (r&#39;what is your name?&#39;, [&quot;I&#39;m just a simple =
chatbot.&quot;, &quot;I&#39;m a chatbot designed to assist you.&quot;]),<br=
>=C2=A0 =C2=A0 (r&#39;bye|goodbye&#39;, [&quot;Goodbye!&quot;, &quot;See yo=
u later!&quot;, &quot;Bye!&quot;]),<br>=C2=A0 =C2=A0 # Add more patterns an=
d responses as needed<br>]<br><br># Create a chatbot<br>chatbot =3D Chat(pa=
tterns, reflections)<br><br># Define a function to chat with the user<br>de=
f chat():<br>=C2=A0 =C2=A0 print(&quot;Hello! How can I assist you today?&q=
uot;)<br>=C2=A0 =C2=A0 while True:<br>=C2=A0 =C2=A0 =C2=A0 =C2=A0 user_inpu=
t =3D input(&quot;&gt; &quot;)<br>=C2=A0 =C2=A0 =C2=A0 =C2=A0 response =3D =
chatbot.respond(user_input)<br>=C2=A0 =C2=A0 =C2=A0 =C2=A0 print(response)<=
br>=C2=A0 =C2=A0 =C2=A0 =C2=A0 if user_input.lower() =3D=3D &#39;bye&#39;:<=
br>=C2=A0 =C2=A0 =C2=A0 =C2=A0 =C2=A0 =C2=A0 break<br><br># Start the chat<=
br>if __name__ =3D=3D &quot;__main__&quot;:<br>=C2=A0 =C2=A0 chat()<br></di=
v>

--000000000000a4633d061b14109c--
