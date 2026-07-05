import os
import requests

def generate_qr_codes():
    print("Generating QR codes for Diya do Mriyi...")
    urls = {
        "website": "https://fil-m.github.io/diya-do-mriyi/",
        "organizer": "https://t.me/robosapiens8"
    }
    
    # Try using qrcode library if installed
    try:
        import qrcode
        print("Using local 'qrcode' library.")
        for name, url in urls.items():
            qr = qrcode.QRCode(version=1, box_size=10, border=1)
            qr.add_data(url)
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white")
            img.save(f"assets/qr_{name}.png")
            print(f"Generated assets/qr_{name}.png")
    except ImportError:
        print("Local 'qrcode' library not found. Fetching from QR Server API...")
        os.makedirs("assets", exist_ok=True)
        for name, url in urls.items():
            api_url = f"https://api.qrserver.com/v1/create-qr-code/?size=300x300&data={url}"
            try:
                response = requests.get(api_url, timeout=10)
                if response.status_code == 200:
                    with open(f"assets/qr_{name}.png", "wb") as f:
                        f.write(response.content)
                    print(f"Downloaded assets/qr_{name}.png")
                else:
                    print(f"Failed to fetch QR code for {name}: HTTP {response.status_code}")
            except Exception as e:
                print(f"Error fetching QR code for {name}: {e}")

def create_html_poster():
    print("Creating HTML poster...")
    html_content = """<!DOCTYPE html>
<html lang="uk">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Дія до мрії — Афіша А4</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800;900&display=swap" rel="stylesheet">
    <style>
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }
        body {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, sans-serif;
            color: #000000;
            background: #ffffff;
            line-height: 1.4;
            padding: 0;
            -webkit-print-color-adjust: exact;
            print-color-adjust: exact;
        }
        
        @page {
            size: A4;
            margin: 12mm 15mm;
        }
        
        .poster-container {
            width: 100%;
            max-width: 210mm;
            min-height: 297mm;
            margin: 0 auto;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }

        /* Header styling */
        .header {
            text-align: center;
            border-bottom: 3px solid #000;
            padding-bottom: 8px;
            margin-bottom: 16px;
        }
        .header-badge {
            display: inline-block;
            border: 2px solid #000;
            padding: 4px 12px;
            font-weight: 700;
            font-size: 13px;
            text-transform: uppercase;
            letter-spacing: 1px;
            margin-bottom: 8px;
        }
        .header h1 {
            font-size: 40px;
            font-weight: 900;
            letter-spacing: -1px;
            text-transform: uppercase;
            line-height: 1.1;
            margin-bottom: 4px;
        }
        .header h1 span {
            background: #000;
            color: #fff;
            padding: 0 8px;
            display: inline-block;
        }
        .header .tagline {
            font-size: 17px;
            font-weight: 600;
            margin-top: 4px;
        }

        /* Main content */
        .main-content {
            flex-grow: 1;
            display: flex;
            flex-direction: column;
            gap: 14px;
        }

        .section-box {
            border: 2px solid #000;
            padding: 12px 16px;
            background: #ffffff;
        }
        
        .section-title {
            font-size: 18px;
            font-weight: 800;
            text-transform: uppercase;
            border-bottom: 2px solid #000;
            padding-bottom: 2px;
            margin-bottom: 8px;
            display: inline-block;
        }

        .core-text {
            font-size: 13.5px;
            line-height: 1.45;
            margin-bottom: 8px;
        }
        .core-text strong {
            font-weight: 700;
        }

        /* Grid layouts */
        .info-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 10px 20px;
        }
        .info-item {
            font-size: 13px;
            line-height: 1.35;
        }
        .info-item strong {
            display: block;
            font-size: 14px;
            font-weight: 700;
            margin-bottom: 2px;
        }

        /* Bullet points */
        .list-items {
            list-style: none;
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 8px 20px;
        }
        .list-items li {
            position: relative;
            padding-left: 18px;
            font-size: 13px;
            line-height: 1.3;
        }
        .list-items li::before {
            content: "✓";
            position: absolute;
            left: 0;
            top: 0;
            font-weight: 800;
            font-size: 14px;
        }
        .list-items li strong {
            font-weight: 700;
        }

        /* Parent Safety Box */
        .safety-box {
            border: 2px dashed #000;
            background: #fdfdfd;
            padding: 12px;
            display: flex;
            align-items: flex-start;
            gap: 10px;
        }
        .safety-icon {
            font-size: 20px;
            line-height: 1;
        }
        .safety-text h3 {
            font-size: 15px;
            font-weight: 800;
            text-transform: uppercase;
            margin-bottom: 2px;
        }
        .safety-text p {
            font-size: 12.5px;
            font-weight: 600;
            line-height: 1.3;
        }

        /* QR section */
        .qr-section {
            border-top: 2px solid #000;
            padding-top: 12px;
            margin-top: 10px;
        }
        .qr-title {
            text-align: center;
            font-size: 14px;
            font-weight: 800;
            text-transform: uppercase;
            margin-bottom: 10px;
        }
        .qr-grid {
            display: flex;
            justify-content: center;
            gap: 60px;
        }
        .qr-card {
            text-align: center;
            max-width: 150px;
        }
        .qr-image-wrapper {
            border: 2px solid #000;
            padding: 4px;
            background: #fff;
            display: inline-block;
            margin-bottom: 4px;
        }
        .qr-card img {
            width: 100px;
            height: 100px;
            display: block;
        }
        .qr-card h4 {
            font-size: 13px;
            font-weight: 700;
            text-transform: uppercase;
            margin-bottom: 2px;
        }
        .qr-card p {
            font-size: 10.5px;
            color: #444;
            line-height: 1.2;
        }

        .footer-note {
            text-align: center;
            font-size: 11px;
            font-weight: 600;
            margin-top: 12px;
            border-top: 1px solid #ddd;
            padding-top: 6px;
        }
        .impressum {
            font-size: 9px;
            font-weight: normal;
            color: #666;
            display: block;
            margin-top: 4px;
        }

        /* Print controls banner */
        .no-print-banner {
            background: #f0f0f0;
            border: 1px solid #ccc;
            padding: 12px;
            margin-bottom: 20px;
            text-align: center;
            font-size: 14px;
        }
        .no-print-banner button {
            background: #000;
            color: #fff;
            border: none;
            padding: 8px 16px;
            font-weight: 700;
            cursor: pointer;
            margin-top: 8px;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
        .no-print-banner button:hover {
            background: #333;
        }

        @media print {
            .no-print-banner {
                display: none !important;
            }
            body {
                padding: 0;
            }
            .poster-container {
                min-height: auto;
            }
        }
    </style>
</head>
<body>

    <div class="no-print-banner">
        <strong>Афіша Дія до мрії підготовлена до друку на форматі A4 (чорно-біла).</strong><br>
        Відкрийте цю сторінку в браузері, натисніть кнопку нижче або комбінацію клавіш <strong>Ctrl + P</strong> і виберіть принтер або збереження в PDF.<br>
        <button onclick="window.print()">Друк / Зберегти як PDF</button>
    </div>

    <div class="poster-container">
        <div class="header">
            <div class="header-badge">Безкоштовно · Для будь-якого віку</div>
            <h1>Дія <span>до</span> мрії</h1>
            <p class="tagline">Напарник для старту. «Ходімо. Зараз перевіримо.»</p>
        </div>

        <div class="main-content">
            <div class="section-box">
                <div class="section-title">У чому суть проекту?</div>
                <p class="core-text">Більшість людей не відкладають ідеї через брак знань — вони відкладають їх, бо <strong>не знають, який перший крок буде правильним</strong>. Я допомагаю зробити цей перший крок на практиці за допомогою маленьких експериментів.</p>
                
                <div class="info-grid">
                    <div class="info-item">
                        <strong>🧒 Дитина з ідеєю</strong>
                        Хоче створити власну гру, робота чи мультфільм. Допоможу зробити першу перевірку на практиці.
                    </div>
                    <div class="info-item">
                        <strong>🧑‍💻 Дорослий з мрією</strong>
                        Давно хочете запустити свій сайт чи проект, але відкладаєте? Розберемося разом без зайвої теорії.
                    </div>
                </div>
            </div>

            <div class="section-box">
                <div class="section-title">З якими проектами я працюю?</div>
                <div class="info-grid" style="grid-template-columns: 1fr 1fr;">
                    <div class="info-item">
                        <strong>💻 Сайти та автоматизація</strong>
                        Створення сайтів, написання коду, автоматизація завдань.
                    </div>
                    <div class="info-item">
                        <strong>🤖 Робототехніка й пристрої</strong>
                        Робота з електронікою, моделювання та збірка простих систем.
                    </div>
                    <div class="info-item">
                        <strong>🎬 Медіа та відеовиробництво</strong>
                        Зйомка відео, монтаж, основи анімації та стопмоушен.
                    </div>
                    <div class="info-item">
                        <strong>🏗️ Конструювання та техніка</strong>
                        Будь-які пристрої чи проекти, які можна зібрати власноруч.
                    </div>
                </div>
            </div>

            <div class="section-box">
                <div class="section-title">Що ти отримаєш після зустрічі?</div>
                <ul class="list-items">
                    <li>
                        <strong>Зрозумілий наступний крок.</strong> Знатимеш, що конкретно робити завтра.
                    </li>
                    <li>
                        <strong>Розуміння, як перевірити ідею</strong> без великих витрат часу чи грошей.
                    </li>
                    <li>
                        <strong>Список потрібних інструментів</strong> та перевірених сервісів саме для твоєї ідеї.
                    </li>
                    <li>
                        <strong>Підтримка напарника.</strong> Людина, якій можна написати, якщо застрягнеш.
                    </li>
                </ul>
            </div>

            <div class="safety-box">
                <div class="safety-icon">🔒</div>
                <div class="safety-text">
                    <h3>Безпека неповнолітніх та супровід батьків</h3>
                    <p>Для дітей та підлітків (до 18 років) присутність або письмова згода батьків/опікунів на першій зустрічі є обов'язковою. Уся комунікація є абсолютно прозорою та відкритою для батьків.</p>
                </div>
            </div>
        </div>

        <div class="qr-section">
            <div class="qr-title">Всього 3 вільні місця для старту. Напиши та забронювати місце:</div>
            <div class="qr-grid">
                <div class="qr-card">
                    <div class="qr-image-wrapper">
                        <img src="assets/qr_website.png" alt="QR Website">
                    </div>
                    <h4>Сайт проекту</h4>
                    <p>Історії старту, детальний FAQ та філософія дій</p>
                </div>
                
                <div class="qr-card">
                    <div class="qr-image-wrapper">
                        <img src="assets/qr_organizer.png" alt="QR Contact">
                    </div>
                    <h4>Зв'язатися</h4>
                    <p>Напиши організатору в Telegram: @robosapiens8</p>
                </div>
            </div>
        </div>

        <div class="footer-note">
            Дія до мрії · Безкоштовна некомерційна ініціатива · Karlsruhe
            <span class="impressum">Impressum: Viktor Serdyuk, c/o Ukrainer in Karlsruhe e.V., Gellertstraße 14, 76185 Karlsruhe | welcomeinkarlsruhe@gmail.com</span>
        </div>
    </div>

</body>
</html>
"""
    with open("poster.html", "w", encoding="utf-8") as f:
        f.write(html_content)
    print("Created poster.html")

def create_pdf_poster():
    print("Creating PDF poster...")
    try:
        from reportlab.lib.pagesizes import A4
        from reportlab.lib.units import mm
        from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image
        from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
        from reportlab.lib import colors
        from reportlab.pdfbase import pdfmetrics
        from reportlab.pdfbase.ttfonts import TTFont
    except ImportError:
        print("Reportlab not available. Cannot generate PDF directly. Use HTML poster and print as PDF.")
        return

    # Check for Arial font on Windows
    arial_path = "C:\\Windows\\Fonts\\arial.ttf"
    arial_bold_path = "C:\\Windows\\Fonts\\arialbd.ttf"
    
    if os.path.exists(arial_path) and os.path.exists(arial_bold_path):
        pdfmetrics.registerFont(TTFont('Arial', arial_path))
        pdfmetrics.registerFont(TTFont('Arial-Bold', arial_bold_path))
        FONT_NORMAL = 'Arial'
        FONT_BOLD = 'Arial-Bold'
        print("Using system Arial font for Cyrillic support.")
    else:
        FONT_NORMAL = 'Helvetica'
        FONT_BOLD = 'Helvetica-Bold'
        print("Arial font not found. Falling back to Helvetica (Cyrillic characters might not render).")

    doc = SimpleDocTemplate(
        "diya_do_mriyi_poster_a4.pdf",
        pagesize=A4,
        rightMargin=15*mm,
        leftMargin=15*mm,
        topMargin=12*mm,
        bottomMargin=12*mm
    )

    styles = getSampleStyleSheet()

    # Define custom styles
    title_p1_style = ParagraphStyle('T1', parent=styles['Normal'], fontName=FONT_BOLD, fontSize=28, leading=32, alignment=2)
    title_p2_style = ParagraphStyle('T2', parent=styles['Normal'], fontName=FONT_BOLD, fontSize=28, leading=32, alignment=1)
    
    badge_style = ParagraphStyle('Badge', parent=styles['Normal'], fontName=FONT_BOLD, fontSize=10, leading=12, alignment=1)
    tagline_style = ParagraphStyle('Tagline', parent=styles['Normal'], fontName=FONT_BOLD, fontSize=12, leading=15, alignment=1)
    
    sec_title_style = ParagraphStyle('SecTitle', parent=styles['Normal'], fontName=FONT_BOLD, fontSize=11.5, leading=13.5, spaceAfter=3)
    body_style = ParagraphStyle('BodyTextCustom', parent=styles['Normal'], fontName=FONT_NORMAL, fontSize=8.5, leading=11)
    core_text_style = ParagraphStyle('CoreTextCustom', parent=styles['Normal'], fontName=FONT_NORMAL, fontSize=9, leading=12)
    
    detail_bold_style = ParagraphStyle('DetailBold', parent=styles['Normal'], fontName=FONT_BOLD, fontSize=9, leading=11)
    detail_body_style = ParagraphStyle('DetailBody', parent=styles['Normal'], fontName=FONT_NORMAL, fontSize=8.5, leading=11)
    
    list_item_style = ParagraphStyle('ListItemStyle', parent=styles['Normal'], fontName=FONT_NORMAL, fontSize=8.5, leading=11)
    
    security_title_style = ParagraphStyle('SecurTitle', parent=styles['Normal'], fontName=FONT_BOLD, fontSize=10.5, leading=12.5, spaceAfter=1)
    security_body_style = ParagraphStyle('SecurBody', parent=styles['Normal'], fontName=FONT_BOLD, fontSize=9, leading=11.5)
    
    qr_title_style = ParagraphStyle('QRTitle', parent=styles['Normal'], fontName=FONT_BOLD, fontSize=10, leading=12, alignment=1)
    qr_label_style = ParagraphStyle('QRLabel', parent=styles['Normal'], fontName=FONT_BOLD, fontSize=9, leading=11, alignment=1)
    qr_desc_style = ParagraphStyle('QRDesc', parent=styles['Normal'], fontName=FONT_NORMAL, fontSize=8, leading=9.5, alignment=1)
    
    footer_style = ParagraphStyle('FooterStyle', parent=styles['Normal'], fontName=FONT_NORMAL, fontSize=7.5, leading=9, alignment=1, textColor=colors.HexColor('#555555'))

    story = []

    # 1. Header Badge
    badge_p = Paragraph("БЕЗКОШТОВНО · ДЛЯ БУДЬ-ЯКОГО ВІКУ", badge_style)
    badge_table = Table([[badge_p]], colWidths=[80*mm])
    badge_table.setStyle(TableStyle([
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('BOX', (0,0), (-1,-1), 1.5, colors.black),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
    ]))
    badge_table.hAlign = 'CENTER'
    story.append(badge_table)
    story.append(Spacer(1, 3*mm))

    # 2. Main Title: ДІЯ ДО МРІЇ
    title_p1 = Paragraph("ДІЯ", title_p1_style)
    title_p2 = Paragraph("<font color=white>ДО МРІЇ</font>", title_p2_style)
    title_table = Table([[title_p1, title_p2]], colWidths=[38*mm, 32*mm])
    title_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('BACKGROUND', (1,0), (1,0), colors.black),
        ('TOPPADDING', (0,0), (-1,-1), 2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
        ('LEFTPADDING', (1,0), (1,0), 6),
        ('RIGHTPADDING', (1,0), (1,0), 6),
    ]))
    title_table.hAlign = 'CENTER'
    story.append(title_table)
    story.append(Spacer(1, 2.5*mm))

    # Tagline
    story.append(Paragraph("Напарник для старту. «Ходімо. Зараз перевіримо.»", tagline_style))
    story.append(Spacer(1, 2.5*mm))

    # Thin line under header
    line_table = Table([[""]], colWidths=[176*mm], rowHeights=[2])
    line_table.setStyle(TableStyle([
        ('LINEBELOW', (0,0), (-1,-1), 2, colors.black),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(line_table)
    story.append(Spacer(1, 4*mm))

    # 3. Section 1: Core Idea
    sec1_content = [
        [Paragraph("У ЧОМУ СУТЬ ПРОЕКТУ?", sec_title_style), ""],
        [Paragraph("Більшість людей не відкладають ідеї через брак знань — вони відкладають їх, бо <b>не знають, який перший крок буде правильним</b>. Я допомагаю зробити цей перший крок на практиці за допомогою маленьких експериментів.", core_text_style), ""],
        [
            Paragraph("<b>🧒 Дитина з ідеєю</b><br/>Хоче створити власну гру, робота чи мультфільм. Допоможу зробити першу перевірку на практиці.", body_style),
            Paragraph("<b>🧑‍💻 Дорослий з мрією</b><br/>Давно хочете запустити свій сайт чи проект, але відкладаєте? Розберемося разом без зайвої теорії.", body_style)
        ]
    ]
    sec1_table = Table(sec1_content, colWidths=[88*mm, 88*mm])
    sec1_table.setStyle(TableStyle([
        ('SPAN', (0,0), (1,0)),
        ('SPAN', (0,1), (1,1)),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BOX', (0,0), (-1,-1), 1.5, colors.black),
        ('TOPPADDING', (0,0), (-1,0), 6),
        ('BOTTOMPADDING', (0,0), (-1,0), 2),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
        ('BOTTOMPADDING', (0,-1), (-1,-1), 8),
        ('TOPPADDING', (0,1), (-1,-1), 4),
        ('BOTTOMPADDING', (0,1), (-1,-2), 6),
    ]))
    sec1_table.hAlign = 'CENTER'
    story.append(sec1_table)
    story.append(Spacer(1, 4*mm))

    # 4. Section 2: Domains we work with
    sec2_content = [
        [Paragraph("З ЯКИМИ ПРОЕКТАМИ Я ПРАЦЮЮ?", sec_title_style), ""],
        [
            Paragraph("<b>💻 Сайти та автоматизація</b><br/>Створення сайтів, написання коду, автоматизація рутинних завдань.", body_style),
            Paragraph("<b>🤖 Робототехніка й пристрої</b><br/>Робота з електронікою, платами, моделювання та збірка простих систем.", body_style)
        ],
        [
            Paragraph("<b>🎬 Медіа та відеовиробництво</b><br/>Зйомка відео, монтаж, основи анімації та стопмоушен.", body_style),
            Paragraph("<b>🏗️ Конструювання та техніка</b><br/>Будь-які пристрої чи проекти, які можна зібрати власноруч.", body_style)
        ]
    ]
    sec2_table = Table(sec2_content, colWidths=[88*mm, 88*mm])
    sec2_table.setStyle(TableStyle([
        ('SPAN', (0,0), (1,0)),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BOX', (0,0), (-1,-1), 1.5, colors.black),
        ('TOPPADDING', (0,0), (-1,0), 6),
        ('BOTTOMPADDING', (0,0), (-1,0), 2),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
        ('BOTTOMPADDING', (0,-1), (-1,-1), 8),
        ('TOPPADDING', (0,1), (-1,-1), 4),
        ('BOTTOMPADDING', (0,1), (-1,-2), 4),
    ]))
    sec2_table.hAlign = 'CENTER'
    story.append(sec2_table)
    story.append(Spacer(1, 4*mm))

    # 5. Section 3: What you get (bullet list)
    sec3_content = [
        [Paragraph("ЩО ТИ ОТРИМАЄШ ПІСЛЯ ЗУСТРІЧІ?", sec_title_style), ""],
        [
            Paragraph("<b>✓ Зрозумілий наступний крок.</b> Ти знатимеш, що конкретно робити завтра — без паніки і теорії.", list_item_style),
            Paragraph("<b>✓ Розуміння, як перевірити ідею</b> без великих витрат часу чи грошей.", list_item_style)
        ],
        [
            Paragraph("<b>✓ Список інструментів та сервісів,</b> які реально потрібні для старту твого проекту.", list_item_style),
            Paragraph("<b>✓ Підтримку напарника,</b> якому можна просто написати, якщо застрягнеш або пропаде мотивація.", list_item_style)
        ]
    ]
    sec3_table = Table(sec3_content, colWidths=[88*mm, 88*mm])
    sec3_table.setStyle(TableStyle([
        ('SPAN', (0,0), (1,0)),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BOX', (0,0), (-1,-1), 1.5, colors.black),
        ('TOPPADDING', (0,0), (-1,0), 6),
        ('BOTTOMPADDING', (0,0), (-1,0), 2),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
        ('BOTTOMPADDING', (0,-1), (-1,-1), 8),
        ('TOPPADDING', (0,1), (-1,-1), 4),
        ('BOTTOMPADDING', (0,1), (-1,-2), 4),
    ]))
    sec3_table.hAlign = 'CENTER'
    story.append(sec3_table)
    story.append(Spacer(1, 4*mm))

    # 6. Safety Box (GDPR / Parent Consent)
    security_p1 = Paragraph("Безпека неповнолітніх та супровід батьків", security_title_style)
    security_p2 = Paragraph("Для дітей та підлітків (до 18 років) присутність або письмова згода батьків/опікунів на першій зустрічі є обов'язковою. Уся комунікація є абсолютно прозорою та відкритою для батьків.", security_body_style)
    
    security_table = Table([[security_p1], [security_p2]], colWidths=[176*mm])
    security_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('BOX', (0,0), (-1,-1), 1.5, colors.black),
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#f9f9f9')),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
    ]))
    security_table.hAlign = 'CENTER'
    story.append(security_table)
    story.append(Spacer(1, 4*mm))

    # Helper function to frame images tightly
    def make_boxed_image(path):
        img = Image(path, width=22*mm, height=22*mm)
        t = Table([[img]], colWidths=[24*mm], rowHeights=[24*mm])
        t.setStyle(TableStyle([
            ('ALIGN', (0,0), (-1,-1), 'CENTER'),
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
            ('BOX', (0,0), (-1,-1), 1, colors.black),
            ('LEFTPADDING', (0,0), (-1,-1), 0),
            ('RIGHTPADDING', (0,0), (-1,-1), 0),
            ('TOPPADDING', (0,0), (-1,-1), 0),
            ('BOTTOMPADDING', (0,0), (-1,-1), 0),
        ]))
        return t

    # 7. QR Section
    story.append(Paragraph("Всього 3 вільні місця для старту. Напиши та забронювати місце:", qr_title_style))
    story.append(Spacer(1, 3*mm))

    qr1 = make_boxed_image("assets/qr_website.png")
    qr2 = make_boxed_image("assets/qr_organizer.png")

    qr_table_data = [
        [qr1, qr2],
        [
            Paragraph("САЙТ ПРОЕКТУ", qr_label_style),
            Paragraph("ЗВ'ЯЗАТИСЯ", qr_label_style)
        ],
        [
            Paragraph("Історії старту, детальний FAQ та філософія дій", qr_desc_style),
            Paragraph("Напиши організатору в Telegram: @robosapiens8", qr_desc_style)
        ]
    ]
    qr_table = Table(qr_table_data, colWidths=[88*mm, 88*mm])
    qr_table.setStyle(TableStyle([
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BOTTOMPADDING', (0,0), (-1,0), 3),
        ('BOTTOMPADDING', (0,1), (-1,1), 1),
        ('TOPPADDING', (0,1), (-1,-1), 3),
    ]))
    qr_table.hAlign = 'CENTER'
    story.append(qr_table)
    story.append(Spacer(1, 4*mm))

    # Separator line
    sep_table = Table([[""]], colWidths=[176*mm], rowHeights=[1])
    sep_table.setStyle(TableStyle([
        ('LINEBELOW', (0,0), (-1,-1), 1, colors.HexColor('#dddddd')),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(sep_table)
    story.append(Spacer(1, 3*mm))

    # 8. Footer
    footer_p = Paragraph("Дія до мрії · Безкоштовна некомерційна ініціатива · Karlsruhe<br/><font size=6.5 color='#666666'>Impressum: Viktor Serdyuk, c/o Ukrainer in Karlsruhe e.V., Gellertstraße 14, 76185 Karlsruhe | welcomeinkarlsruhe@gmail.com</font>", footer_style)
    story.append(footer_p)

    doc.build(story)
    print("Created diya_do_mriyi_poster_a4.pdf")

if __name__ == "__main__":
    os.makedirs("assets", exist_ok=True)
    generate_qr_codes()
    create_html_poster()
    create_pdf_poster()
