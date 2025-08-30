from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch, mm
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.platypus.flowables import HRFlowable

def create_professional_resume():
    # Create PDF with professional margins
    doc = SimpleDocTemplate("resume.pdf", pagesize=A4, 
                          rightMargin=15*mm, leftMargin=15*mm,
                          topMargin=15*mm, bottomMargin=15*mm)
    
    styles = getSampleStyleSheet()
    
    # Professional styles
    title_style = ParagraphStyle(
        'Title', fontSize=28, spaceAfter=3, alignment=TA_CENTER,
        textColor=colors.HexColor('#1a365d'), fontName='Helvetica-Bold', letterSpacing=2
    )
    
    subtitle_style = ParagraphStyle(
        'Subtitle', fontSize=16, spaceAfter=8, alignment=TA_CENTER,
        textColor=colors.HexColor('#2b6cb0'), fontName='Helvetica', letterSpacing=1
    )
    
    heading_style = ParagraphStyle(
        'Heading', fontSize=13, spaceAfter=8, spaceBefore=16,
        textColor=colors.white, fontName='Helvetica-Bold',
        backColor=colors.HexColor('#2b6cb0'), borderPadding=8, letterSpacing=1
    )
    
    job_style = ParagraphStyle(
        'Job', fontSize=12, spaceAfter=2, textColor=colors.HexColor('#1a365d'), fontName='Helvetica-Bold'
    )
    
    company_style = ParagraphStyle(
        'Company', fontSize=10, spaceAfter=6, textColor=colors.HexColor('#4a5568'), fontName='Helvetica-Oblique'
    )
    
    bullet_style = ParagraphStyle(
        'Bullet', fontSize=10, spaceAfter=3, leftIndent=15, textColor=colors.HexColor('#2d3748')
    )
    
    summary_style = ParagraphStyle(
        'Summary', fontSize=11, spaceAfter=12, textColor=colors.HexColor('#2d3748'), 
        alignment=TA_JUSTIFY, leading=14
    )
    
    content = []
    
    # Header
    content.append(Paragraph("DARSHAN N", title_style))

    content.append(Paragraph("AI/ML Engineer", subtitle_style))
    content.append(HRFlowable(width="100%", thickness=2, color=colors.HexColor('#2b6cb0')))
    content.append(Spacer(2, 8))
    
    # Contact Info
    contact_data = [
        ["✉ darshan.nagaraju2001@gmail.com", "☎ +91 9008405328"],
        ["🌐 https://www.linkedin.com/in/darshan-n-0b2253196?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_contact_details%3BLFzlH03OQwOOkZONGXA%2FAA%3D%3D", "📍 Bengaluru, Karnataka, India"]
    ]
    
    contact_table = Table(contact_data, colWidths=[95*mm, 95*mm])
    contact_table.setStyle(TableStyle([
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('FONTSIZE', (0,0), (-1,-1), 10),
        ('FONTNAME', (0,0), (-1,-1), 'Helvetica'),
        ('TEXTCOLOR', (0,0), (-1,-1), colors.HexColor('#4a5568')),
        ('ROWBACKGROUNDS', (0,0), (-1,-1), [colors.HexColor('#f7fafc')]),
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor('#e2e8f0')),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#e2e8f0')),
        ('TOPPADDING', (0,0), (-1,-1), 8),
        ('BOTTOMPADDING', (0,0), (-1,-1), 8)
    ]))
    content.append(contact_table)
    content.append(Spacer(1, 16))
    
    # Professional Summary
    content.append(Paragraph("PROFESSIONAL SUMMARY", heading_style))
    summary = """Accomplished AI/ML Engineer with 1+ years of expertise in Machine Learning, Deep Learning, and Computer Vision. 
    Proven track record in developing cutting-edge AI solutions including GPT-4 integrated systems, Azure cloud deployments, 
    and enterprise-level applications. Specialized in building scalable AI pipelines, automated recruitment systems, and 
    real-time analytics platforms with strong focus on compliance and security."""
    content.append(Paragraph(summary, summary_style))
    
    # Experience
    content.append(Paragraph("PROFESSIONAL EXPERIENCE", heading_style))
    
    # GradientM
    content.append(Paragraph("AI/ML Engineer | GradientM IT Consulting & Services Pvt Ltd", job_style))
    content.append(Paragraph("May 2025 - Present | Bengaluru, Karnataka | 4.6⭐ Rating", company_style))
    
    gradient_points = [
        "Built and deployed AI-powered Applicant Tracking System with advanced resume parsing and intelligent deduplication",
        "Developed Resume Evaluation System with GPT-4 integration featuring 6-criteria scoring and automated decision-making",
        "Implemented end-to-end candidate lifecycle management with real-time analytics dashboard and SLA tracking",
        "Created comprehensive compliance framework with Azure cloud integration, audit trails, and data security protocols",
        "Successfully deployed production applications on Azure App Service with responsive UI and multi-format file processing"
    ]
    for point in gradient_points:
        content.append(Paragraph(f"• {point}", bullet_style))
    content.append(Spacer(1, 8))
    
    # BotRecruits
    content.append(Paragraph("AIML Developer (Freelancer) | BotRecruits Software Private Limited", job_style))
    content.append(Paragraph("November 2024 - March 2025 | Bengaluru, Karnataka", company_style))
    
    bot_points = [
        "Developed intelligent AI chatbot for StaffingGO application, resulting in 40% improvement in user engagement",
        "Integrated AWS SNS notifications system, enabling real-time communication and reducing response time by 60%",
        "Implemented serverless AWS Lambda automation for payment workflows, email processing, and notification systems"
    ]
    for point in bot_points:
        content.append(Paragraph(f"• {point}", bullet_style))
    content.append(Spacer(1, 8))
    
    # Velospear
    content.append(Paragraph("Machine Learning Engineer | Velospear Technologies", job_style))
    content.append(Paragraph("February 2024 - September 2024 | Bengaluru, Karnataka", company_style))
    
    velo_points = [
        "Led ML/DL/AI initiatives for advanced theft detection systems, achieving 35% reduction in security incidents",
        "Developed cutting-edge generative AI model using LLaVA and GPT-4o for comprehensive threat analysis and reporting",
        "Integrated high-performance multistream pipeline on Deepstream Nano device for real-time video processing",
        "Implemented robust AWS S3 data handling and publishing infrastructure supporting scalable data management workflows"
    ]
    for point in velo_points:
        content.append(Paragraph(f"• {point}", bullet_style))
    content.append(Spacer(1, 12))
    
    # Technical Skills
    content.append(Paragraph("TECHNICAL SKILLS", heading_style))
    
    skills_data = [
        ["Microsoft Azure", "Azure Bot Services, Functions, Cognitive Services, OpenAI, AI Search, Storage, App Service"],
        ["AI/ML Technologies", "Machine Learning, Deep Learning, Computer Vision, Generative AI, Threat Analysis, NLP"],
        ["AI Libraries & Frameworks", "PyTorch, TensorFlow, Keras, Pandas, NumPy, Matplotlib, Scikit-learn"],
        ["Cloud & Deployment", "AWS (S3, Lambda, SNS, SQS), Deepstream, Jetson Nano, Docker, Kubernetes"],
        ["Model Integration", "LLaVA, GPT-4o, Azure OpenAI, Data Annotation, Pipeline Deployment, MLOps"],
        ["Programming & Database", "Python, SQL, MySQL, PostgreSQL, Git, GitHub, REST APIs, Microservices"]
    ]
    
    skills_table = Table(skills_data, colWidths=[40*mm, 130*mm])
    skills_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (0,-1), colors.HexColor('#2b6cb0')),
        ('TEXTCOLOR', (0,0), (0,-1), colors.white),
        ('TEXTCOLOR', (1,0), (1,-1), colors.HexColor('#2d3748')),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('FONTSIZE', (0,0), (-1,-1), 10),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('FONTNAME', (0,0), (0,-1), 'Helvetica-Bold'),
        ('FONTNAME', (1,0), (1,-1), 'Helvetica'),
        ('GRID', (0,0), (-1,-1), 1, colors.HexColor('#e2e8f0')),
        ('ROWBACKGROUNDS', (1,0), (1,-1), [colors.HexColor('#f7fafc'), colors.white]),
        ('TOPPADDING', (0,0), (-1,-1), 8),
        ('BOTTOMPADDING', (0,0), (-1,-1), 8),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10)
    ]))
    content.append(skills_table)
    content.append(Spacer(1, 12))
    
    # Key Projects
    content.append(Paragraph("KEY PROJECTS", heading_style))
    
    project_style = ParagraphStyle(
        'Project', fontSize=11, spaceAfter=2, textColor=colors.HexColor('#1a365d'), fontName='Helvetica-Bold'
    )
    
    project_desc_style = ParagraphStyle(
        'ProjectDesc', fontSize=10, spaceAfter=8, textColor=colors.HexColor('#4a5568'), leftIndent=10
    )
    
    projects = [
        ("AI-Powered Resume Evaluation System (Azure Deployed)", 
         "Enterprise-grade system with GPT-4 integration, 6-criteria intelligent scoring, multi-format processing (PDF/DOCX/TXT), automated shortlist/reject decisions, and professional branded reporting"),
        ("Centralized Applicant Tracking System (Production)", 
         "Full-stack recruitment platform with AI resume parsing, natural language chatbot interface, automated lifecycle management, compliance framework, and real-time analytics dashboard"),
        ("Advanced Threat Analysis & Weapon Detection", 
         "Real-time computer vision system with facial recognition, database integration, threat classification, and security incident reporting for enterprise applications"),
        ("Smart Road Safety AI Platform", 
         "Intelligent traffic monitoring system with accident prediction algorithms, real-time analysis, IoT integration, and automated alert mechanisms")
    ]
    
    for project_name, project_desc in projects:
        content.append(Paragraph(f"▶ {project_name}", project_style))
        content.append(Paragraph(project_desc, project_desc_style))
    
    # Education
    content.append(Paragraph("EDUCATION", heading_style))
    content.append(Paragraph("Bachelor of Engineering - Computer Science and Engineering", job_style))
    content.append(Paragraph("Jyothy Institute of Technology, Bangalore | July 2019 - June 2023", company_style))
    content.append(Spacer(1, 8))
    
    # Certifications
    content.append(Paragraph("PROFESSIONAL CERTIFICATIONS", heading_style))
    certs = [
        "Deep Learning with PyTorch: Advanced Image Segmentation",
        "Image Classification with TensorFlow: Production Implementation",
        "Machine Learning Pipelines with Azure ML Studio",
        "Business Analysis & Process Management",
        "Deep Learning with PyTorch: Generative Adversarial Networks",
        "Ethical Hacking Certification - Python & SQL Security"
    ]
    for cert in certs:
        content.append(Paragraph(f"🏆 {cert}", bullet_style))
    
    # Build PDF
    doc.build(content)
    print("✅ Professional resume created successfully as 'resume.pdf'")
    print("📄 Features: Modern design, ATS-friendly format, professional styling")

if __name__ == "__main__":
    create_professional_resume()