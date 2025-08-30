from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.platypus.flowables import HRFlowable
from reportlab.graphics.shapes import Drawing, Circle
from reportlab.graphics import renderPDF
import os

# Delete existing file if it exists
if os.path.exists("resume.pdf"):
    try:
        os.remove("resume.pdf")
    except:
        pass

# Create PDF
doc = SimpleDocTemplate("Darshan_Resume_Updated_About.pdf", pagesize=A4, 
                      rightMargin=15*mm, leftMargin=15*mm,
                      topMargin=15*mm, bottomMargin=15*mm)

styles = getSampleStyleSheet()

# Professional styles
title_style = ParagraphStyle(
    'Title', fontSize=24, spaceAfter=8, alignment=TA_CENTER,
    textColor=colors.HexColor('#1a365d'), fontName='Helvetica-Bold'
)

subtitle_style = ParagraphStyle(
    'Subtitle', fontSize=14, spaceAfter=12, alignment=TA_CENTER,
    textColor=colors.HexColor('#2b6cb0'), fontName='Helvetica'
)

heading_style = ParagraphStyle(
    'Heading', fontSize=13, spaceAfter=8, spaceBefore=16,
    textColor=colors.white, fontName='Helvetica-Bold',
    backColor=colors.HexColor('#2b6cb0'), borderPadding=8
)

job_style = ParagraphStyle(
    'Job', fontSize=12, spaceAfter=2, textColor=colors.HexColor('#1a365d'), fontName='Helvetica-Bold'
)

company_style = ParagraphStyle(
    'Company', fontSize=10, spaceAfter=6, textColor=colors.HexColor('#4a5568'), fontName='Helvetica-Oblique'
)

bullet_style = ParagraphStyle(
    'Bullet', fontSize=10, spaceAfter=3, leftIndent=15, textColor=colors.HexColor('#2d3748'), fontName='Helvetica'
)

content = []

# Header with Photo
try:
    # Try to add actual photo
    photo = Image('darshan.jpg', width=35*mm, height=35*mm)
    photo_cell = photo
except:
    # Fallback to placeholder text
    photo_cell = Paragraph("[PHOTO]", ParagraphStyle('PhotoPlaceholder', fontSize=12, 
                          textColor=colors.HexColor('#2b6cb0'), fontName='Helvetica-Bold', alignment=TA_CENTER))

header_data = [[
    photo_cell,
    # Name and title
    Paragraph("DARSHAN N<br/>AI/ML Engineer<br/><font size=10>Machine Learning & Computer Vision Specialist</font>", 
             ParagraphStyle('HeaderText', fontSize=20, textColor=colors.HexColor('#1a365d'), 
                          fontName='Helvetica-Bold', alignment=TA_CENTER, leading=24))
]]

header_table = Table(header_data, colWidths=[40*mm, 130*mm])
header_table.setStyle(TableStyle([
    ('ALIGN', (0,0), (0,0), 'CENTER'),
    ('ALIGN', (1,0), (1,0), 'CENTER'),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('FONTSIZE', (0,0), (0,0), 12),
    ('TEXTCOLOR', (0,0), (0,0), colors.HexColor('#2b6cb0')),
    ('FONTNAME', (0,0), (0,0), 'Helvetica-Bold'),
    ('BOX', (0,0), (0,0), 2, colors.HexColor('#2b6cb0')),
    ('BACKGROUND', (0,0), (0,0), colors.HexColor('#f0f8ff')),
    ('TOPPADDING', (0,0), (-1,-1), 10),
    ('BOTTOMPADDING', (0,0), (-1,-1), 10)
]))
content.append(header_table)
content.append(Spacer(1, 8))
content.append(HRFlowable(width="100%", thickness=2, color=colors.HexColor('#2b6cb0')))
content.append(Spacer(1, 12))

# Contact Info
contact_data = [
    ["Email: darshan.nagaraju2001@gmail.com", "Phone: +91 9008405328"],
    ["LinkedIn: linkedin.com/in/darshan-n-0b2253196/", "Location: Bengaluru, Karnataka, India"]
]

contact_table = Table(contact_data, colWidths=[95*mm, 95*mm])
contact_table.setStyle(TableStyle([
    ('ALIGN', (0,0), (-1,-1), 'CENTER'),
    ('FONTSIZE', (0,0), (-1,-1), 10),
    ('TEXTCOLOR', (0,0), (-1,-1), colors.HexColor('#4a5568')),
    ('ROWBACKGROUNDS', (0,0), (-1,-1), [colors.HexColor('#f7fafc')]),
    ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor('#e2e8f0')),
    ('TOPPADDING', (0,0), (-1,-1), 8),
    ('BOTTOMPADDING', (0,0), (-1,-1), 8)
]))
content.append(contact_table)
content.append(Spacer(1, 16))

# Professional Summary
content.append(Paragraph("PROFESSIONAL SUMMARY", heading_style))
summary = """Experienced Software Engineer with expertise in Machine Learning, Computer Vision, and Generative AI. 
Skilled in developing secure, scalable solutions using Python and Flask, with clean UI design, real-time data handling, 
and automated CI/CD deployment via GitHub. Proficient in building document automation tools, resume evaluators, 
and data-driven platforms using Azure OpenAI and cloud technologies."""

summary_style = ParagraphStyle('Summary', fontSize=10, spaceAfter=12, textColor=colors.HexColor('#2d3748'), alignment=TA_JUSTIFY, fontName='Helvetica')
content.append(Paragraph(summary, summary_style))

# Experience
content.append(Paragraph("PROFESSIONAL EXPERIENCE", heading_style))

# GradientM
content.append(Paragraph("AI/ML Engineer | GradientM IT Consulting & Services Pvt Ltd", job_style))
content.append(Paragraph("May 2025 - Present | Bengaluru, Karnataka | 4.6 Star Rating", company_style))

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
    ["Microsoft Azure", "Azure Bot Services, Functions, Cognitive Services, OpenAI, AI Search, Storage"],
    ["AI/ML Technologies", "Machine Learning, Deep Learning, Computer Vision, Generative AI, NLP"],
    ["AI Libraries", "PyTorch, TensorFlow, Keras, Pandas, NumPy, Matplotlib"],
    ["Cloud & Deployment", "AWS (S3, Lambda, SNS), Deepstream, Jetson Nano, Docker"],
    ["Model Integration", "LLaVA, GPT-4o, Azure OpenAI, Data Annotation"],
    ["Programming", "Python, SQL, MySQL, Git, GitHub, REST APIs"]
]

skills_table = Table(skills_data, colWidths=[38*mm, 125*mm])
skills_table.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (0,-1), colors.HexColor('#2b6cb0')),
    ('TEXTCOLOR', (0,0), (0,-1), colors.white),
    ('TEXTCOLOR', (1,0), (1,-1), colors.HexColor('#2d3748')),
    ('ALIGN', (0,0), (-1,-1), 'LEFT'),
    ('FONTSIZE', (0,0), (-1,-1), 9),
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ('FONTNAME', (0,0), (0,-1), 'Helvetica-Bold'),
    ('FONTNAME', (1,0), (1,-1), 'Helvetica'),
    ('GRID', (0,0), (-1,-1), 1, colors.HexColor('#e2e8f0')),
    ('TOPPADDING', (0,0), (-1,-1), 6),
    ('BOTTOMPADDING', (0,0), (-1,-1), 6),
    ('LEFTPADDING', (0,0), (-1,-1), 8),
    ('RIGHTPADDING', (0,0), (-1,-1), 8)
]))
content.append(skills_table)
content.append(Spacer(1, 12))

# Portfolio Section
content.append(Paragraph("PROJECT PORTFOLIO", heading_style))

# Portfolio projects in table format
portfolio_data = [
    ["🚀 AI-Powered Resume Evaluation System", "Azure Deployed | GPT-4 Integration", "Production"],
    ["📊 Centralized Applicant Tracking System", "Full-stack Platform | Real-time Analytics", "Live"],
    ["🔒 Threat Analysis & Weapon Detection", "Computer Vision | Security Applications", "Deployed"],
    ["🛣️ Smart Road Safety AI Platform", "IoT Integration | Predictive Analytics", "Active"]
]

portfolio_table = Table(portfolio_data, colWidths=[70*mm, 70*mm, 25*mm])
portfolio_table.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#2b6cb0')),
    ('TEXTCOLOR', (0,0), (-1,0), colors.white),
    ('ALIGN', (0,0), (-1,-1), 'LEFT'),
    ('ALIGN', (2,0), (2,-1), 'CENTER'),
    ('FONTSIZE', (0,0), (-1,-1), 9),
    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
    ('FONTNAME', (0,1), (-1,-1), 'Helvetica'),
    ('GRID', (0,0), (-1,-1), 1, colors.HexColor('#e2e8f0')),
    ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.HexColor('#f8f9fa'), colors.white]),
    ('TOPPADDING', (0,0), (-1,-1), 8),
    ('BOTTOMPADDING', (0,0), (-1,-1), 8),
    ('LEFTPADDING', (0,0), (-1,-1), 8)
]))
content.append(portfolio_table)
content.append(Spacer(1, 8))

# Key Achievements
content.append(Paragraph("KEY ACHIEVEMENTS", heading_style))
achievements = [
    "🏆 Successfully deployed 2 enterprise AI applications on Azure App Service",
    "📈 Achieved 40% improvement in user engagement through AI chatbot development", 
    "🔧 Reduced security incidents by 35% using advanced ML/DL threat detection",
    "⚡ Improved response time by 60% through AWS SNS integration",
    "🎯 Built GPT-4 powered resume evaluation with 6-criteria automated scoring"
]

for achievement in achievements:
    content.append(Paragraph(achievement, bullet_style))
content.append(Spacer(1, 8))

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
print("Professional resume created: Darshan_Resume_Updated_About.pdf")