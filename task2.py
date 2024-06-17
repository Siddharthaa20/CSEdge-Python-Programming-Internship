Delivered-To: siddharthaarepalli46@gmail.com
Received: by 2002:a59:552:0:b0:463:f90a:5760 with SMTP id 79csp1802327vqf;
        Mon, 17 Jun 2024 04:13:52 -0700 (PDT)
X-Received: by 2002:a05:600c:a42:b0:421:5966:ca40 with SMTP id 5b1f17b1804b1-42304826f4dmr84917245e9.10.1718622831976;
        Mon, 17 Jun 2024 04:13:51 -0700 (PDT)
ARC-Seal: i=1; a=rsa-sha256; t=1718622831; cv=none;
        d=google.com; s=arc-20160816;
        b=sQ7gF4YKsrXHFkRXsO5LSvRazRFA7xsuqz63Jca0XmbrmYHd2ZuofWlEQaFQg1oj/U
         QI/BuZesnwvMAiP7tR215acKh5VIPXLloSST8pGAgk9VXVg4kWKwAp/F8NDa4AY+YElN
         t6TCsin3rUqYndJ4zvTlGR2IL+X8er5bR7gHJPRUZqb49Dk0TN2zJ5fE+SQP6cypWSx6
         GjsJMHB2haVkJr/fUs7IhPMK9QHB1aSCfuQWdYwENQZjOBXcuzVRYC0EEs0qWXq+b4k9
         /e40yZjG383HHxJBMRhPM9Vu/rhhx30MrnDZqo4hGW9vddfg/QW+EYSPj1ENLy1q0QhE
         ugvA==
ARC-Message-Signature: i=1; a=rsa-sha256; c=relaxed/relaxed; d=google.com; s=arc-20160816;
        h=to:subject:message-id:date:from:mime-version:dkim-signature;
        bh=haIGDwb2mlYS3BFNZv42OAvZzdxk06jKQ9mpQqkRAqM=;
        fh=ogtUl7XzfsmBwMTFbUaql7G2PHzPz+ca7PDOvyDOPpk=;
        b=S8PgSawV+Tp3aZP6dtFEIc1yDdX3bXFPXKaDfOrmlZuTjawdg5xlUQZiiiQjJhdI6a
         4llA4hg5MUswEEwoTR87AUP6wZuMyCiYDF7IsZKwycKjNu5tcjA4Q5vlKkADiF7gfiUN
         wJot1xbWl7Pwxqq8vlh/bPlHThUrs18HCZiXZ1Kgd5X5nPX7jhsBFDIEkU5NQTUWUag5
         aNeJnmfnl5OSNi/UUDF+vmoQM7wsF3Ux1QPoWPqJS+4RSIjhNWXU6yBH+mP4hEW1QnT8
         +9klMAmtW08gwTygEQSwq0L569xDb9F6SGwCzd06S5k5k4hh7D9loffWnR8UgTd2Sk6r
         /cqQ==;
        dara=google.com
ARC-Authentication-Results: i=1; mx.google.com;
       dkim=pass header.i=@gmail.com header.s=20230601 header.b=mUZ5yYHm;
       spf=pass (google.com: domain of meghanakankati24@gmail.com designates 209.85.220.41 as permitted sender) smtp.mailfrom=meghanakankati24@gmail.com;
       dmarc=pass (p=NONE sp=QUARANTINE dis=NONE) header.from=gmail.com
Return-Path: <meghanakankati24@gmail.com>
Received: from mail-sor-f41.google.com (mail-sor-f41.google.com. [209.85.220.41])
        by mx.google.com with SMTPS id 5b1f17b1804b1-422f6229391sor26008565e9.9.2024.06.17.04.13.51
        for <siddharthaarepalli46@gmail.com>
        (Google Transport Security);
        Mon, 17 Jun 2024 04:13:51 -0700 (PDT)
Received-SPF: pass (google.com: domain of meghanakankati24@gmail.com designates 209.85.220.41 as permitted sender) client-ip=209.85.220.41;
Authentication-Results: mx.google.com;
       dkim=pass header.i=@gmail.com header.s=20230601 header.b=mUZ5yYHm;
       spf=pass (google.com: domain of meghanakankati24@gmail.com designates 209.85.220.41 as permitted sender) smtp.mailfrom=meghanakankati24@gmail.com;
       dmarc=pass (p=NONE sp=QUARANTINE dis=NONE) header.from=gmail.com
DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/relaxed;
        d=gmail.com; s=20230601; t=1718622831; x=1719227631; dara=google.com;
        h=to:subject:message-id:date:from:mime-version:from:to:cc:subject
         :date:message-id:reply-to;
        bh=haIGDwb2mlYS3BFNZv42OAvZzdxk06jKQ9mpQqkRAqM=;
        b=mUZ5yYHmyKHq751w3eQuhAbAlUFgKv68QP3YgcHzmt6c/aTAatcOuRfFHkSySX9nTU
         dN9d/mlsF/ChXqsq7MmaCk3+fbTKTHTAp6KMPjGlTbMUpfhBOYagnnGzvpapRVVrhyky
         xI9fCkpdvfGo2mPZ8ATfnxmWTImNqL9Q02P/0kdmXgZJsz/NfXyI3hKbq4L2pvj3k+nj
         Frz8iSa2vk13Wz+SGPsHYwOuzjX8BIMo8KcDsX8EXZtZjAZfVaSGDvUxQdiC01EZcjvM
         FFBHBjgoSRAeiZHIGwYMZkyKoDuijYGrQ9Dy4f8t3+8WmXj+3gW2WAE5Cb1PtxXmLl8v
         hm4Q==
X-Google-DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/relaxed;
        d=1e100.net; s=20230601; t=1718622831; x=1719227631;
        h=to:subject:message-id:date:from:mime-version:x-gm-message-state
         :from:to:cc:subject:date:message-id:reply-to;
        bh=haIGDwb2mlYS3BFNZv42OAvZzdxk06jKQ9mpQqkRAqM=;
        b=C1rG7+Abv5ep/i0jrqfhdyQkwZX/RsV5Q9r5EVguUY4Jc56+kGdR5jX5/LmDVy2/gw
         c0w2zBB/9YS852E+XkbDQKqmcTddfbObOhVWwgTiHZG6vAUMpJ+DzxrdfQ+/gHSJAQfN
         asOu7IKGraDyoVhDepho5JfAk8IWAZq4P7HN6jk338M3zWGTe4/NRvx3Z2czqBgNbTrX
         JO19DlxPGEHj3OVqZDtqdfprWg4X6w+PvvNUHmPspny5zm/I/DChWQiCS44j9Z6okprl
         Jq9HFFyBVEowTLm0xMWtGs5q/ARKFWEnJzwDpQTKIoZ1AO57hfNg+i9lUd1hwICcGjGJ
         uaow==
X-Gm-Message-State: AOJu0YxnluEO0rNHSR3JKqVxd6cV5J5jPEGykBv2PqFxdINvRVQI3aWB
	aOshZ/mVrhobgk4mLCGIakGks4aM5O4tYBDikFRtT+ad80mTeOwL131QoEu3hP2bySQJKD3c6G0
	I62Ac5a6ErpdR5+B+vfAa560paynbLpf0
X-Google-Smtp-Source: AGHT+IHwh1P3vlFMW4/a+3JsuAt+s67J2rFc+GrmqPcz+DjuKTuMEE815DuJF0R81zf9RDHPwo0ozAnreBkeK3wp1Os=
X-Received: by 2002:a5d:6901:0:b0:360:8269:5690 with SMTP id
 ffacd0b85a97d-36082695cdamr5635177f8f.17.1718622831069; Mon, 17 Jun 2024
 04:13:51 -0700 (PDT)
MIME-Version: 1.0
From: Meghana _k <meghanakankati24@gmail.com>
Date: Mon, 17 Jun 2024 16:43:38 +0530
Message-ID: <CAB1d5xLssDd0_xaNJwjura+uJUzEr+k24Xz9-10MHnD-NqHieA@mail.gmail.com>
Subject: task2
To: AREPALLI SIDDHARTHA <siddharthaarepalli46@gmail.com>
Content-Type: multipart/alternative; boundary="000000000000595591061b140f16"

--000000000000595591061b140f16
Content-Type: text/plain; charset="UTF-8"

import requests
from bs4 import BeautifulSoup
import csv
import json

def scrape_website(url):
    # Send a GET request to the URL
    response = requests.get(url)

    # Parse HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    titles = [title.text.strip() for title in soup.find_all('h1')]

    return titles

def save_to_csv(data, filename):
    # Write data to a CSV file
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
       writer = csv.writer(csvfile)
       writer.writerow(['Title'])
       writer.writerows(data)

def save_to_json(data, filename):
    # Write data to a JSON file
    with open(filename, 'w', encoding='utf-8') as jsonfile:
        json.dump(data, jsonfile, indent=4)

def main( ):
    url = input("Enter the URL of the website you want to scrape: ")


    output_format = input("Enter 'csv' or 'json' to choose the output
format: ").lower()
    if output_format not in ['csv','json']:
        print("Invalid output format. Please enter 'csv' or 'json'.")
        return
    extracted_data = scrape_website(url)
    if output_format == 'csv':
        filename = input("Enter the filename to store the data (without
extension): ") + '.csv'
        save_to_csv(extracted_data, filename)
        print(f"Data has been saved to {filename}")
    elif output_format == 'json':
        filename = input("Enter the filename to store the data (without
extension): ") + '.json'
        save_to_json(extracted_data, filename)
        print(f"Data has been saved to {filename}")
if __name__ == "__main__":
    main()

--000000000000595591061b140f16
Content-Type: text/html; charset="UTF-8"
Content-Transfer-Encoding: quoted-printable

<div dir=3D"ltr">import requests<br>from bs4 import BeautifulSoup<br>import=
 csv<br>import json<br><br>def scrape_website(url):<br>=C2=A0 =C2=A0 # Send=
 a GET request to the URL<br>=C2=A0 =C2=A0 response =3D requests.get(url)<b=
r>=C2=A0 =C2=A0 <br>=C2=A0 =C2=A0 # Parse HTML content<br>=C2=A0 =C2=A0 sou=
p =3D BeautifulSoup(response.text, &#39;html.parser&#39;)<br>=C2=A0 =C2=A0 =
<br>=C2=A0 =C2=A0 titles =3D [title.text.strip() for title in soup.find_all=
(&#39;h1&#39;)]<br>=C2=A0 =C2=A0 <br>=C2=A0 =C2=A0 return titles<br><br>def=
 save_to_csv(data, filename):<br>=C2=A0 =C2=A0 # Write data to a CSV file<b=
r>=C2=A0 =C2=A0 with open(filename, &#39;w&#39;, newline=3D&#39;&#39;, enco=
ding=3D&#39;utf-8&#39;) as csvfile:<br>=C2=A0 =C2=A0 =C2=A0 =C2=A0writer =
=3D csv.writer(csvfile)<br>=C2=A0 =C2=A0 =C2=A0 =C2=A0writer.writerow([&#39=
;Title&#39;])<br>=C2=A0 =C2=A0 =C2=A0 =C2=A0writer.writerows(data)<br><br>d=
ef save_to_json(data, filename):<br>=C2=A0 =C2=A0 # Write data to a JSON fi=
le<br>=C2=A0 =C2=A0 with open(filename, &#39;w&#39;, encoding=3D&#39;utf-8&=
#39;) as jsonfile:<br>=C2=A0 =C2=A0 =C2=A0 =C2=A0 json.dump(data, jsonfile,=
 indent=3D4)<br><br>def main( ):<br>=C2=A0 =C2=A0 url =3D input(&quot;Enter=
 the URL of the website you want to scrape: &quot;)<br>=C2=A0 =C2=A0 <br>=
=C2=A0 =C2=A0 <br>=C2=A0 =C2=A0 output_format =3D input(&quot;Enter &#39;cs=
v&#39; or &#39;json&#39; to choose the output format: &quot;).lower()<br>=
=C2=A0 =C2=A0 if output_format not in [&#39;csv&#39;,&#39;json&#39;]:<br>=
=C2=A0 =C2=A0 =C2=A0 =C2=A0 print(&quot;Invalid output format. Please enter=
 &#39;csv&#39; or &#39;json&#39;.&quot;)<br>=C2=A0 =C2=A0 =C2=A0 =C2=A0 ret=
urn<br>=C2=A0 =C2=A0 extracted_data =3D scrape_website(url)<br>=C2=A0 =C2=
=A0 if output_format =3D=3D &#39;csv&#39;:<br>=C2=A0 =C2=A0 =C2=A0 =C2=A0 f=
ilename =3D input(&quot;Enter the filename to store the data (without exten=
sion): &quot;) + &#39;.csv&#39;<br>=C2=A0 =C2=A0 =C2=A0 =C2=A0 save_to_csv(=
extracted_data, filename)<br>=C2=A0 =C2=A0 =C2=A0 =C2=A0 print(f&quot;Data =
has been saved to {filename}&quot;)<br>=C2=A0 =C2=A0 elif output_format =3D=
=3D &#39;json&#39;:<br>=C2=A0 =C2=A0 =C2=A0 =C2=A0 filename =3D input(&quot=
;Enter the filename to store the data (without extension): &quot;) + &#39;.=
json&#39;<br>=C2=A0 =C2=A0 =C2=A0 =C2=A0 save_to_json(extracted_data, filen=
ame)<br>=C2=A0 =C2=A0 =C2=A0 =C2=A0 print(f&quot;Data has been saved to {fi=
lename}&quot;)<br>if __name__ =3D=3D &quot;__main__&quot;:<br>=C2=A0 =C2=A0=
 main()<br>=C2=A0 =C2=A0 =C2=A0 =C2=A0=C2=A0<br></div>

--000000000000595591061b140f16--
