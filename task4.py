Delivered-To: siddharthaarepalli46@gmail.com
Received: by 2002:a59:552:0:b0:463:f90a:5760 with SMTP id 79csp1802620vqf;
        Mon, 17 Jun 2024 04:14:35 -0700 (PDT)
X-Received: by 2002:a5d:61c3:0:b0:360:9533:c716 with SMTP id ffacd0b85a97d-3609533c932mr1946434f8f.2.1718622875046;
        Mon, 17 Jun 2024 04:14:35 -0700 (PDT)
ARC-Seal: i=1; a=rsa-sha256; t=1718622875; cv=none;
        d=google.com; s=arc-20160816;
        b=t3bhTKzm8DN9HcR0AB/d4/rbLCH3uz/E6l/aRr3vtFQVKLyk2lK/kEH5FutKvUcZhN
         LgIS8YTXi2xuTbeRU0JfMmwbh6UJCTCI9xnB1N85LGrBeqaMjTm51YOcEl67gebmUch7
         6lURYw3/85xXsj8b0AiQhMfm7n7PIdFSxFwxapacQTYTZBoN7CVYQcmYtk3AVKfQVSaY
         qSTfR8fvo3g8r9entiM6CKA6N1ByUtOOaHd/5jAWfHzplLvZhSkJDDgzWwx9XM98otAA
         U5j91ZtWScPuvtC83/84kIhuZ86TjBP/xmo48ZYR+uCgIOEC0F1InTF50u4mqDYCyt0+
         JiuQ==
ARC-Message-Signature: i=1; a=rsa-sha256; c=relaxed/relaxed; d=google.com; s=arc-20160816;
        h=to:subject:message-id:date:from:mime-version:dkim-signature;
        bh=fLXccTrXeMF4Ds6J2ZWO74/Wr1XGuP6XhO6j3T86XNk=;
        fh=ogtUl7XzfsmBwMTFbUaql7G2PHzPz+ca7PDOvyDOPpk=;
        b=wbtpCap8Co9MtG4pXt06PzdvlJjmrbWKtB2LHYvatXa2jEhvqfM/6f/cPOn5j29UGn
         wSHpdq+FxCTYE6Qva2j+eGTdqWSe7BJjWCbeumBSKKIDzJskQwsHJdgkNzJHwusIkdLm
         OsRxwbch2QqmHuDhq+mK8kl/2ZIqY0ZTCPM7EBeAnb8t6h4TbqGeQ+qxu/uHcYMheI0o
         35oQmBaTAnPi953NXr1Y9YTBsGzPG03QGIORhHb2nkjgWHE1IKFGuL/KiXucCDCshaY7
         5DswriY9Sglmqq1zr9OfcRTM0qefXf8HSpJBwDFRsFVlLD3y/hxlpqH88iS/eo38a9U2
         MHtA==;
        dara=google.com
ARC-Authentication-Results: i=1; mx.google.com;
       dkim=pass header.i=@gmail.com header.s=20230601 header.b=ixXu8KKM;
       spf=pass (google.com: domain of meghanakankati24@gmail.com designates 209.85.220.41 as permitted sender) smtp.mailfrom=meghanakankati24@gmail.com;
       dmarc=pass (p=NONE sp=QUARANTINE dis=NONE) header.from=gmail.com
Return-Path: <meghanakankati24@gmail.com>
Received: from mail-sor-f41.google.com (mail-sor-f41.google.com. [209.85.220.41])
        by mx.google.com with SMTPS id ffacd0b85a97d-360750fb3b8sor2361984f8f.6.2024.06.17.04.14.34
        for <siddharthaarepalli46@gmail.com>
        (Google Transport Security);
        Mon, 17 Jun 2024 04:14:35 -0700 (PDT)
Received-SPF: pass (google.com: domain of meghanakankati24@gmail.com designates 209.85.220.41 as permitted sender) client-ip=209.85.220.41;
Authentication-Results: mx.google.com;
       dkim=pass header.i=@gmail.com header.s=20230601 header.b=ixXu8KKM;
       spf=pass (google.com: domain of meghanakankati24@gmail.com designates 209.85.220.41 as permitted sender) smtp.mailfrom=meghanakankati24@gmail.com;
       dmarc=pass (p=NONE sp=QUARANTINE dis=NONE) header.from=gmail.com
DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/relaxed;
        d=gmail.com; s=20230601; t=1718622874; x=1719227674; dara=google.com;
        h=to:subject:message-id:date:from:mime-version:from:to:cc:subject
         :date:message-id:reply-to;
        bh=fLXccTrXeMF4Ds6J2ZWO74/Wr1XGuP6XhO6j3T86XNk=;
        b=ixXu8KKM9Vv3otEbmsJmR5vi3GqTZjY1A2TCgXNZ0L5ELb5QlJuiuPCdoAfjx2Fqyh
         LDWoTEpfhu1QuWci2jqpOJ0UeE34UQL6GBEOU/64+qLSr6EvNnBqthnFkkV2LfVTXD4p
         kgqn8haeCAyD4rNp9PcbJ5sczS2IfCJoQj03RTdcuT1IFpuXZ9NyN7dQOB7e47M/iiiH
         2XUTkWrWkio37DshKlsjRN/n2pGz8pZAAiB7FkdUlVfJmlTvbxhspbHfP9X1fPFDEpOI
         H+INIgkgDJL3KZArKVAc8I1QIGTXeCzYldk4yB7xfqoY+v5ZaUmIXwsMkBFZNqzYYyAF
         4B4w==
X-Google-DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/relaxed;
        d=1e100.net; s=20230601; t=1718622874; x=1719227674;
        h=to:subject:message-id:date:from:mime-version:x-gm-message-state
         :from:to:cc:subject:date:message-id:reply-to;
        bh=fLXccTrXeMF4Ds6J2ZWO74/Wr1XGuP6XhO6j3T86XNk=;
        b=vDhozxx4fsBLtHXzserAGyPEHHdA0BGdjjmiPRD4TZnncB2PWbCGAFkTwG19VavvJ6
         2/KCo4W7Y20xYNjruYKlcRUM+BmAA8DxgBaeYnuFpfz1Mp3jM74LD+bU2/voJqkgzL+b
         xA/xr5QLzGMJmKvRQx0R/W8ZkHEKRCKAg1C0UqsiSCQhOp/njZo88AOD7dwXicutODpk
         ILwCDDG72R9MWHjQV4CONFqkkkqiQrmT/TaQiioEZe9soXUhK/wDgE6OdIaZ+cxseTo8
         7Yf5zIk/2borZvIZyVas7xNstcVHeETlPS+3fTB8JncrAtz2YQ+nJ99Mv7QUwMjoNIEg
         U35Q==
X-Gm-Message-State: AOJu0YwYPjhMpfZEMeCQD+C+dLZADUGoYuhqK5gALZdWf+Yv/xZs21FJ
	UFK5cjgvbra86ZtznqaW4dgjPC5zADNE1ZjxN/3yXbujdCL2fMKFOHsDvw1RDpJDxc6I1f/87gv
	4UrpSppp8IMobgWVm7gjP6CPYa4EKGbCu
X-Google-Smtp-Source: AGHT+IFTBeRGBwujV3MGbBgOsfySct3qPasuSBLZdBTAAuLxVBB0NbhKMxRq0Hl0zbCTY5Gy3kSKQwQ11ZAuxr0j/NU=
X-Received: by 2002:a5d:4e42:0:b0:35f:1c34:adfc with SMTP id
 ffacd0b85a97d-3607a78db97mr6669691f8f.67.1718622874258; Mon, 17 Jun 2024
 04:14:34 -0700 (PDT)
MIME-Version: 1.0
From: Meghana _k <meghanakankati24@gmail.com>
Date: Mon, 17 Jun 2024 16:44:22 +0530
Message-ID: <CAB1d5xLC4AJrrLOeqsOqZNCHNhQ2oMxX4iT7ubNgFYwgVOYTew@mail.gmail.com>
Subject: task4
To: AREPALLI SIDDHARTHA <siddharthaarepalli46@gmail.com>
Content-Type: multipart/alternative; boundary="000000000000ec56b2061b1411a1"

--000000000000ec56b2061b1411a1
Content-Type: text/plain; charset="UTF-8"

import PyPDF2
import os

def merge_pdfs(input_paths, output_path):
    pdf_writer = PyPDF2.PdfWriter()

    for path in input_paths:
        pdf_reader = PyPDF2.PdfReader(path)
        for page in pdf_reader.pages:
            pdf_writer.add_page(page)

    with open(output_path, 'wb') as out_pdf:
        pdf_writer.write(out_pdf)

def split_pdf(input_path, output_folder):
    pdf_reader = PyPDF2.PdfReader(input_path)

    for i, page in enumerate(pdf_reader.pages):
        pdf_writer = PyPDF2.PdfWriter()
        pdf_writer.add_page(page)

        output_path = os.path.join(output_folder, f'page_{i+1}.pdf')
        with open(output_path, 'wb') as out_pdf:
            pdf_writer.write(out_pdf)

# Example usage:
# Merge PDFs
input_files = ['file1.pdf', 'file2.pdf']
output_merged = 'merged.pdf'
merge_pdfs(input_files, output_merged)

# Split PDF
input_pdf = 'large_file.pdf'
output_folder = 'split_pages'
split_pdf(input_pdf, output_folder)

--000000000000ec56b2061b1411a1
Content-Type: text/html; charset="UTF-8"
Content-Transfer-Encoding: quoted-printable

<div dir=3D"ltr">import PyPDF2<br>import os<br><br>def merge_pdfs(input_pat=
hs, output_path):<br>=C2=A0 =C2=A0 pdf_writer =3D PyPDF2.PdfWriter()<br>=C2=
=A0 =C2=A0 <br>=C2=A0 =C2=A0 for path in input_paths:<br>=C2=A0 =C2=A0 =C2=
=A0 =C2=A0 pdf_reader =3D PyPDF2.PdfReader(path)<br>=C2=A0 =C2=A0 =C2=A0 =
=C2=A0 for page in pdf_reader.pages:<br>=C2=A0 =C2=A0 =C2=A0 =C2=A0 =C2=A0 =
=C2=A0 pdf_writer.add_page(page)<br>=C2=A0 =C2=A0 <br>=C2=A0 =C2=A0 with op=
en(output_path, &#39;wb&#39;) as out_pdf:<br>=C2=A0 =C2=A0 =C2=A0 =C2=A0 pd=
f_writer.write(out_pdf)<br><br>def split_pdf(input_path, output_folder):<br=
>=C2=A0 =C2=A0 pdf_reader =3D PyPDF2.PdfReader(input_path)<br>=C2=A0 =C2=A0=
 <br>=C2=A0 =C2=A0 for i, page in enumerate(pdf_reader.pages):<br>=C2=A0 =
=C2=A0 =C2=A0 =C2=A0 pdf_writer =3D PyPDF2.PdfWriter()<br>=C2=A0 =C2=A0 =C2=
=A0 =C2=A0 pdf_writer.add_page(page)<br>=C2=A0 =C2=A0 =C2=A0 =C2=A0 <br>=C2=
=A0 =C2=A0 =C2=A0 =C2=A0 output_path =3D os.path.join(output_folder, f&#39;=
page_{i+1}.pdf&#39;)<br>=C2=A0 =C2=A0 =C2=A0 =C2=A0 with open(output_path, =
&#39;wb&#39;) as out_pdf:<br>=C2=A0 =C2=A0 =C2=A0 =C2=A0 =C2=A0 =C2=A0 pdf_=
writer.write(out_pdf)<br><br># Example usage:<br># Merge PDFs<br>input_file=
s =3D [&#39;file1.pdf&#39;, &#39;file2.pdf&#39;]<br>output_merged =3D &#39;=
merged.pdf&#39;<br>merge_pdfs(input_files, output_merged)<br><br># Split PD=
F<br>input_pdf =3D &#39;large_file.pdf&#39;<br>output_folder =3D &#39;split=
_pages&#39;<br>split_pdf(input_pdf, output_folder)<br></div>

--000000000000ec56b2061b1411a1--
