from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY

def create_resume():
    # Create PDF document
    doc = SimpleDocTemplate("resume.pdf", pagesize=A4, 
                          rightMargin=0.5*inch, leftMargin=0.5*inch,
                          topMargin=0.5*inch, bottomMargin=0.5*inch)
    
    # Get styles and create custom styles
    styles = getSampleStyleSheet()
    
    # Custom styles
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        spaceAfter=6,
        alignment=TA_CENTER,
        textColor=colors.HexColor('#2c3e50')
    )
    
    subtitle_style = ParagraphStyle(
        'CustomSubtitle',
        parent=styles['Normal'],
        fontSize=14,
        spaceAfter=12,
        alignment=TA_CENTER,
        textColor=colors.HexColor('#3498db')
    )
    
    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=14,
        spaceAfter=6,
        spaceBefore=12,
        textColor=colors.HexColor('#2c3e50'),
        borderWidth=1,
        borderColor=colors.HexColor('#3498db'),
        borderPadding=3,
        backColor=colors.HexColor('#ecf0f1')
    )
    
    content = []
    
    # Header
    content.append(Paragraph("DARSHAN N", title_style))
    content.append(Paragraph("AI/ML Engineer", subtitle_style))
    
    # Contact Info
    contact_data = [
        ["📧 darshan.nagaraju2001@gmail.com", "📱 +91 9008405328"],
        ["🔗 linkedin.com/in/darshan-n-0b2253196/", "📍 Bengaluru, Karnataka"]
    ]
    
    contact_table = Table(contact_data, colWidths=[3*inch, 3*inch])
    contact_table.setStyle(TableStyle([
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('FONTSIZE', (0,0), (-1,-1), 10),
        ('TEXTCOLOR', (0,0), (-1,-1), colors.HexColor('#34495e')),
    ]))
    content.append(contact_table)
    content.append(Spacer(1, 12))
    
    # Summary
    content.append(Paragraph("PROFESSIONAL SUMMARY", heading_style))
    summary_text = """Accomplished Software Engineer with 1+ years of expertise in Machine Learning, Deep Learning, and Computer Vision. 
    Proven track record in developing cutting-edge AI solutions, Azure cloud integration, and enterprise-level applications. 
    Strong problem-solving skills with deep understanding of AI frameworks and deployment strategies."""
    content.append(Paragraph(summary_text, styles['Normal']))
    content.append(Spacer(1, 12))
    
    # Experience
    content.append(Paragraph("PROFESSIONAL EXPERIENCE", heading_style))
    
    # GradientM
    content.append(Paragraph("<b>AI/ML Engineer</b> | GradientM IT Consulting & Services Pvt Ltd", styles['Heading3']))
    content.append(Paragraph("<i>May 2025 - Present | Bengaluru, Karnataka</i>", styles['Normal']))
    gradient_points = [
        "• Built and deployed AI-powered Applicant Tracking System with resume parsing and deduplication",
        "• Developed Resume Evaluation System with GPT-4 integration and 6-criteria scoring framework",
        "• Implemented automated candidate lifecycle management with real-time analytics dashboard",
        "• Created compliance framework with Azure cloud integration and secure processing",
        "• Deployed applications on Azure App Service with responsive UI and multi-format support"
    ]
    for point in gradient_points:
        content.append(Paragraph(point, styles['Normal']))
    content.append(Spacer(1, 8))
    
    # BotRecruits
    content.append(Paragraph("<b>AIML Developer (Freelancer)</b> | BotRecruits Software Private Limited", styles['Heading3']))
    content.append(Paragraph("<i>November 2024 - March 2025 | Bengaluru, Karnataka</i>", styles['Normal']))
    bot_points = [
        "• Developed AI chatbot for StaffingGO app, enhancing user interaction and engagement",
        "• Integrated SNS notifications improving real-time user communication systems",
        "• Implemented AWS Lambda automation for payment workflows and email processing"
    ]
    for point in bot_points:
        content.append(Paragraph(point, styles['Normal']))
    content.append(Spacer(1, 8))
    
    # Velospear
    content.append(Paragraph("<b>Machine Learning Engineer</b> | Velospear Technologies", styles['Heading3']))
    content.append(Paragraph("<i>February 2024 - September 2024 | Bengaluru, Karnataka</i>", styles['Normal']))
    velo_points = [
        "• Led ML/DL/AI initiatives for theft detection systems, reducing security incidents",
        "• Developed generative AI model using LLaVA and GPT-4o for threat analysis",
        "• Integrated multistream pipeline on Deepstream Nano device for real-time processing",
        "• Implemented S3 Bucket data handling and publishing for scalable data management"
    ]
    for point in velo_points:
        content.append(Paragraph(point, styles['Normal']))
    content.append(Spacer(1, 12))
    
    # Technical Skills
    content.append(Paragraph("TECHNICAL SKILLS", heading_style))
    
    skills_data = [
        ["Microsoft Azure", "Azure Bot Services, Functions, Cognitive Services, OpenAI, AI Search, Storage"],
        ["AI/ML Technologies", "Machine Learning, Deep Learning, Computer Vision, Generative AI, Threat Analysis"],
        ["AI Libraries", "PyTorch, TensorFlow, Keras, Pandas, NumPy, Matplotlib"],
        ["Cloud & Deployment", "AWS (S3, Lambda, SNS), Deepstream, Jetson Nano, Azure App Service"],
        ["Model Integration", "LLaVA, GPT-4o, Data Annotation, Pipeline Deployment"],
        ["Programming", "Python, SQL, MySQL, Git, GitHub, HTML, CSS"]
    ]
    
    skills_table = Table(skills_data, colWidths=[1.5*inch, 4.5*inch])
    skills_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (0,-1), colors.HexColor('#ecf0f1')),
        ('TEXTCOLOR', (0,0), (0,-1), colors.HexColor('#2c3e50')),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('FONTSIZE', (0,0), (-1,-1), 9),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('FONTNAME', (0,0), (0,-1), 'Helvetica-Bold'),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#bdc3c7')),
        ('ROWBACKGROUNDS', (0,0), (-1,-1), [colors.white, colors.HexColor('#f8f9fa')])
    ]))
    content.append(skills_table)
    content.append(Spacer(1, 12))
    
    # Key Projects
    content.append(Paragraph("KEY PROJECTS", heading_style))
    
    projects = [
        ("AI-Powered Resume Evaluation System", 
         "GPT-4 integration, 6-criteria scoring, multi-format support, automated decisions, Azure deployment"),
        ("Applicant Tracking System", 
         "Resume parsing, chatbot interface, lifecycle management, compliance framework, real-time analytics"),
        ("Threat Analysis & Weapon Detection", 
         "Real-time facial recognition, database integration, security applications"),
        ("Road Safety AI Innovation", 
         "Traffic monitoring, accident prediction, intelligent analysis systems")
    ]
    
    for project_name, project_desc in projects:
        content.append(Paragraph(f"<b>{project_name}</b>", styles['Heading4']))
        content.append(Paragraph(project_desc, styles['Normal']))
        content.append(Spacer(1, 6))
    
    # Education
    content.append(Paragraph("EDUCATION", heading_style))
    content.append(Paragraph("<b>Bachelor of Engineering - Computer Science and Engineering</b>", styles['Heading4']))
    content.append(Paragraph("Jyothy Institute of Technology, Bangalore | July 2019 - June 2023", styles['Normal']))
    content.append(Spacer(1, 8))
    
    # Certifications
    content.append(Paragraph("CERTIFICATIONS", heading_style))
    certs = [
        "• Deep Learning with PyTorch: Image Segmentation",
        "• Basic Image Classification with TensorFlow",
        "• Machine Learning Pipelines with Azure ML Studio",
        "• Business Analysis & Process Management",
        "• Deep Learning with PyTorch: Generative Adversarial Networks",
        "• Ethical Hacker - Python & SQL"
    ]
    for cert in certs:
        content.append(Paragraph(cert, styles['Normal']))
    
    # Build PDF
    doc.build(content)
    print("Resume created successfully as 'resume.pdf'")

if __name__ == "__main__":
    create_resume()