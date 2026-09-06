import sys, os

workspace_dir = os.path.dirname(os.path.abspath(__file__))
pylibs_dir = os.path.join(os.path.dirname(workspace_dir), 'pylibs')
if os.path.exists(pylibs_dir):
    sys.path.insert(0, pylibs_dir)

from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.colors import HexColor
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, Image
)
from reportlab.pdfgen import canvas
from reportlab.graphics.shapes import Drawing, Rect, String, Group, Line, Circle
from reportlab.graphics.charts.piecharts import Pie
from reportlab.graphics.charts.barcharts import VerticalBarChart

# Define Palette
C_FOREST = HexColor('#1b3d2f')
C_OCHRE = HexColor('#c59b27')
C_SLATE = HexColor('#2c3e50')
C_LIGHT = HexColor('#f8faf8')
C_BORDER = HexColor('#e2e8f0')
C_TEXT = HexColor('#1f2937')
C_MUTED = HexColor('#64748b')
C_WHITE = HexColor('#ffffff')
C_TEAL = HexColor('#0d9488')
C_AMBER = HexColor('#d97706')
C_INDIGO = HexColor('#4338ca')

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super().showPage()
        super().save()

    def draw_page_decorations(self, page_count):
        if self._pageNumber == 1:
            self.saveState()
            self.setFillColor(C_FOREST)
            self.rect(0, 830, 595.27, 12, fill=1, stroke=0)
            self.setFillColor(C_OCHRE)
            self.rect(0, 824, 595.27, 6, fill=1, stroke=0)
            self.setStrokeColor(C_OCHRE)
            self.setLineWidth(2)
            self.line(36, 36, 559, 36)
            self.setFont('Helvetica', 7.5)
            self.setFillColor(C_MUTED)
            self.drawString(36, 24, 'Aaranya University Statutory Placement Publication · Academic Year 2025–26')
            self.drawRightString(559, 24, 'Office of Career Development')
            self.restoreState()
            return

        self.saveState()
        self.setFont('Helvetica-Bold', 8)
        self.setFillColor(C_FOREST)
        self.drawString(36, 804, 'AARANYA UNIVERSITY')
        self.setFont('Helvetica', 8)
        self.setFillColor(C_MUTED)
        self.drawString(145, 804, '|   Annual Placement & Career Outcomes Report 2025–2026')
        self.setFont('Helvetica-Bold', 7.5)
        self.setFillColor(C_OCHRE)
        self.drawRightString(559, 804, 'CORPORATE RELATIONS & PLACEMENTS')

        self.setStrokeColor(C_BORDER)
        self.setLineWidth(0.75)
        self.line(36, 796, 559, 796)

        self.line(36, 40, 559, 40)
        self.setFont('Helvetica', 7.5)
        self.setFillColor(C_MUTED)
        self.drawString(36, 28, 'Statutory Charter · Certified Graduate Placement Record · placements@aaranya.edu.in')
        page_str = f'Page {self._pageNumber} of {page_count}'
        self.setFont('Helvetica-Bold', 8)
        self.setFillColor(C_FOREST)
        self.drawRightString(559, 28, page_str)
        self.restoreState()

def create_brochure_pdf(output_path):
    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    doc = SimpleDocTemplate(
        output_path,
        pagesize=A4,
        leftMargin=36,
        rightMargin=36,
        topMargin=36,
        bottomMargin=36
    )

    printable_w = 523.27
    styles = getSampleStyleSheet()

    cover_sup = ParagraphStyle('CoverSup', fontName='Helvetica-Bold', fontSize=8.5, leading=11, textColor=C_OCHRE, spaceAfter=6)
    cover_title = ParagraphStyle('CoverTitle', fontName='Helvetica-Bold', fontSize=22, leading=26, textColor=C_FOREST, spaceAfter=8)
    cover_sub = ParagraphStyle('CoverSub', fontName='Helvetica', fontSize=10, leading=14, textColor=C_MUTED, spaceAfter=12)
    
    h1 = ParagraphStyle('SectionH1', fontName='Helvetica-Bold', fontSize=15, leading=19, textColor=C_FOREST, spaceAfter=4)
    h2 = ParagraphStyle('SectionH2', fontName='Helvetica-Bold', fontSize=11, leading=14, textColor=C_SLATE, spaceBefore=7, spaceAfter=5)
    p_body = ParagraphStyle('BodyTextCustom', fontName='Helvetica', fontSize=8, leading=11, textColor=C_TEXT)
    p_lead = ParagraphStyle('LeadCustom', fontName='Helvetica', fontSize=9, leading=13, textColor=C_MUTED, spaceAfter=8)
    p_table_header = ParagraphStyle('TableHeader', fontName='Helvetica-Bold', fontSize=7.5, leading=9.5, textColor=C_WHITE, alignment=1)
    p_table_cell = ParagraphStyle('TableCell', fontName='Helvetica', fontSize=7, leading=9.5, textColor=C_TEXT)
    p_table_cell_bold = ParagraphStyle('TableCellBold', fontName='Helvetica-Bold', fontSize=7, leading=9.5, textColor=C_FOREST)
    p_table_cell_right = ParagraphStyle('TableCellRight', fontName='Helvetica', fontSize=7, leading=9.5, textColor=C_TEXT, alignment=2)
    p_table_cell_right_bold = ParagraphStyle('TableCellRightBold', fontName='Helvetica-Bold', fontSize=7, leading=9.5, textColor=C_FOREST, alignment=2)

    story = []

    # PAGE 1: COVER
    story.append(Spacer(1, 10))
    story.append(Paragraph('AARANYA UNIVERSITY · OFFICE OF CAREER DEVELOPMENT & ALLIANCES', cover_sup))
    story.append(Paragraph('Annual Placement & Graduate Outcomes Report', cover_title))
    story.append(Paragraph('Graduating Class of 2025–2026 · Comprehensive Salary Distribution, Recruiter Metrics & Corporate Partnerships', cover_sub))

    intl_str = '$165,000'
    metric_box_data = [
        [
            Paragraph('<b><font size="13" color="#1b3d2f">98.8%</font></b><br/><font size="6.5" color="#64748b">OVERALL PLACEMENT RATE<br/>(100% in CS & Design)</font>', p_body),
            Paragraph('<b><font size="13" color="#1b3d2f">₹64.50 LPA</font></b><br/><font size="6.5" color="#64748b">HIGHEST DOMESTIC PACKAGE<br/>(Deep Tech / Systems)</font>', p_body),
            Paragraph(f'<b><font size="13" color="#1b3d2f">{intl_str}</font></b><br/><font size="6.5" color="#64748b">HIGHEST INTL. CTC (₹1.38 CR)<br/>(San Francisco / London)</font>', p_body)
        ],
        [
            Paragraph('<b><font size="13" color="#c59b27">₹21.40 LPA</font></b><br/><font size="6.5" color="#64748b">BATCH AVERAGE CTC<br/>(+28% YoY Growth)</font>', p_body),
            Paragraph('<b><font size="13" color="#1b3d2f">1,482</font></b><br/><font size="6.5" color="#64748b">TOTAL OFFERS EXTENDED<br/>(Across 384 Recruiters)</font>', p_body),
            Paragraph('<b><font size="13" color="#1b3d2f">74%</font></b><br/><font size="6.5" color="#64748b">PPO CONVERSION RATE<br/>(Summer Interns to Full-Time)</font>', p_body)
        ]
    ]
    t_metrics = Table(metric_box_data, colWidths=[printable_w/3.0]*3)
    t_metrics.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), C_LIGHT),
        ('BOX', (0,0), (-1,-1), 1, C_BORDER),
        ('INNERGRID', (0,0), (-1,-1), 0.75, C_BORDER),
        ('TOPPADDING', (0,0), (-1,-1), 7),
        ('BOTTOMPADDING', (0,0), (-1,-1), 7),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
    ]))
    story.append(t_metrics)
    story.append(Spacer(1, 12))

    img_path = os.path.join(workspace_dir, 'assets', 'images', 'placements_overview.jpg')
    if os.path.exists(img_path):
        story.append(Image(img_path, width=printable_w, height=195))
        story.append(Spacer(1, 10))

    foreword_html = '''<b>Foreword from the Director of Career Development:</b><br/>
    The 2025–2026 academic placement season at Aaranya University represents our most successful cohort to date. Grounded in our pedagogical philosophy—<i>Learn, Belong, Become</i>—our students demonstrated unmatched intellectual dexterity and ethical problem-solving across artificial intelligence, quantitative economics, corporate jurisprudence, and transdisciplinary product design. With over 384 premier organizations recruiting on campus, 1,482 offers were secured, yielding an aggregate placement rate of 98.8% and an average compensation of ₹21.40 LPA. This publication serves as an empirical ledger of our graduates' achievements.'''
    
    t_foreword = Table([[Paragraph(foreword_html, p_body)]], colWidths=[printable_w])
    t_foreword.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), HexColor('#f1f5f9')),
        ('BOX', (0,0), (-1,-1), 0.5, HexColor('#cbd5e1')),
        ('LINELEFT', (0,0), (0,-1), 3.5, C_FOREST),
        ('TOPPADDING', (0,0), (-1,-1), 7),
        ('BOTTOMPADDING', (0,0), (-1,-1), 7),
        ('LEFTPADDING', (0,0), (-1,-1), 11),
        ('RIGHTPADDING', (0,0), (-1,-1), 11),
    ]))
    story.append(t_foreword)

    # PAGE 2: SALARY DISTRIBUTION TIERS & SCHOOL MATRIX
    story.append(PageBreak())
    story.append(Paragraph('Academic Architecture & Salary Tiers', h1))
    story.append(Paragraph('Empirical distribution of compensation packages and cross-school performance benchmarks for the 2025–26 recruitment drive.', p_lead))

    tier_data = [
        [Paragraph('Compensation Tier', p_table_header), Paragraph('CTC Range', p_table_header), Paragraph('Cohort Share', p_table_header), Paragraph('Primary Industry Sectors', p_table_header), Paragraph('Sample Recruiters', p_table_header)],
        [Paragraph('Tier 1 (Marquee & Global)', p_table_cell_bold), Paragraph('₹30.0 – ₹64.5+ LPA', p_table_cell), Paragraph('34% of Cohort', p_table_cell_bold), Paragraph('Deep AI, Quant Trading, Top-Tier Strategy', p_table_cell), Paragraph('Google, Apple, Goldman Sachs, BCG, Atlassian', p_table_cell)],
        [Paragraph('Tier 2 (Super-Dream)', p_table_cell_bold), Paragraph('₹20.0 – ₹30.0 LPA', p_table_cell), Paragraph('41% of Cohort', p_table_cell_bold), Paragraph('Product Tech, FinTech, Corporate Law M&A', p_table_cell), Paragraph('Microsoft, Amazon, J.P. Morgan, Shardul Amarchand', p_table_cell)],
        [Paragraph('Tier 3 (Dream)', p_table_cell_bold), Paragraph('₹14.0 – ₹20.0 LPA', p_table_cell), Paragraph('21% of Cohort', p_table_cell_bold), Paragraph('Enterprise Systems, Strategy Consulting', p_table_cell), Paragraph('Deloitte, KPMG, Hyundai Labs, Frog Design', p_table_cell)],
        [Paragraph('Tier 4 (Core Practice)', p_table_cell_bold), Paragraph('₹10.0 – ₹14.0 LPA', p_table_cell), Paragraph('4% of Cohort', p_table_cell_bold), Paragraph('Policy Research, Public Interest Law, Media', p_table_cell), Paragraph('CPR, Trilegal Appellate, Tata R&D, NGOs', p_table_cell)],
    ]
    t_tier = Table(tier_data, colWidths=[105, 80, 65, 135, 138])
    t_tier.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), C_FOREST),
        ('BOX', (0,0), (-1,-1), 1, C_BORDER),
        ('INNERGRID', (0,0), (-1,-1), 0.5, C_BORDER),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [C_WHITE, C_LIGHT]),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(t_tier)
    story.append(Spacer(1, 12))

    story.append(Paragraph('School-Wise Placement Performance Matrix', h2))
    school_data = [
        [Paragraph('Collegiate School', p_table_header), Paragraph('Graduates', p_table_header), Paragraph('Placement %', p_table_header), Paragraph('Highest CTC', p_table_header), Paragraph('Average CTC', p_table_header), Paragraph('Median CTC', p_table_header), Paragraph('PPO %', p_table_header)],
        [Paragraph('<b>School of Computer Science</b><br/><font size="6" color="#64748b">B.Tech, B.Sc, M.Sc, Ph.D</font>', p_body), Paragraph('320', p_table_cell_right), Paragraph('<b>100.0%</b>', p_table_cell_right_bold), Paragraph('₹64.50 LPA', p_table_cell_right), Paragraph('₹26.80 LPA', p_table_cell_right_bold), Paragraph('₹23.50 LPA', p_table_cell_right), Paragraph('82%', p_table_cell_right)],
        [Paragraph('<b>School of Business & Economics</b><br/><font size="6" color="#64748b">B.B.A, B.Sc Econ, B.A Soc, M.Sc</font>', p_body), Paragraph('290', p_table_cell_right), Paragraph('<b>99.1%</b>', p_table_cell_right_bold), Paragraph('₹44.00 LPA', p_table_cell_right), Paragraph('₹22.50 LPA', p_table_cell_right_bold), Paragraph('₹19.40 LPA', p_table_cell_right), Paragraph('76%', p_table_cell_right)],
        [Paragraph('<b>School of Design & Innovation</b><br/><font size="6" color="#64748b">B.Des (4 Tracks), M.Des, Ph.D</font>', p_body), Paragraph('180', p_table_cell_right), Paragraph('<b>100.0%</b>', p_table_cell_right_bold), Paragraph('₹38.50 LPA', p_table_cell_right), Paragraph('₹19.60 LPA', p_table_cell_right_bold), Paragraph('₹17.20 LPA', p_table_cell_right), Paragraph('78%', p_table_cell_right)],
        [Paragraph('<b>School of Law</b><br/><font size="6" color="#64748b">5-Yr B.A. LL.B, 3-Yr LL.B, LL.M</font>', p_body), Paragraph('210', p_table_cell_right), Paragraph('<b>97.8%</b>', p_table_cell_right_bold), Paragraph('₹34.00 LPA', p_table_cell_right), Paragraph('₹18.40 LPA', p_table_cell_right_bold), Paragraph('₹16.00 LPA', p_table_cell_right), Paragraph('68%', p_table_cell_right)],
        [Paragraph('<b>Liberal Arts & Sciences</b><br/><font size="6" color="#64748b">Humanities, Social Sci, Natural Sci</font>', p_body), Paragraph('240', p_table_cell_right), Paragraph('<b>96.5%</b>', p_table_cell_right_bold), Paragraph('₹28.00 LPA', p_table_cell_right), Paragraph('₹15.80 LPA', p_table_cell_right_bold), Paragraph('₹14.20 LPA', p_table_cell_right), Paragraph('62%', p_table_cell_right)],
        [Paragraph('<b>University Aggregate</b>', p_body), Paragraph('<b>1,240</b>', p_table_cell_right_bold), Paragraph('<b>98.8%</b>', p_table_cell_right_bold), Paragraph('<b>₹64.50 LPA</b>', p_table_cell_right_bold), Paragraph('<b>₹21.40 LPA</b>', p_table_cell_right_bold), Paragraph('<b>₹18.20 LPA</b>', p_table_cell_right_bold), Paragraph('<b>74%</b>', p_table_cell_right_bold)],
    ]
    t_school = Table(school_data, colWidths=[163, 55, 65, 60, 60, 60, 60])
    t_school.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), C_FOREST),
        ('BOX', (0,0), (-1,-1), 1, C_BORDER),
        ('INNERGRID', (0,0), (-1,-1), 0.5, C_BORDER),
        ('ROWBACKGROUNDS', (0,1), (-1,-2), [C_WHITE, C_LIGHT]),
        ('BACKGROUND', (0,-1), (-1,-1), HexColor('#e6f0eb')),
        ('TOPPADDING', (0,0), (-1,-1), 3.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3.5),
    ]))
    story.append(t_school)
    story.append(Spacer(1, 12))

    story.append(Paragraph('Average vs Median CTC by School (in ₹ Lakhs Per Annum)', h2))
    d_bar = Drawing(printable_w, 125)
    d_bar.add(Rect(0, 0, printable_w, 125, fillColor=C_LIGHT, strokeColor=C_BORDER, strokeWidth=0.5, rx=3, ry=3))
    
    bc = VerticalBarChart()
    bc.x = 45
    bc.y = 20
    bc.height = 90
    bc.width = 440
    bc.data = [
        [26.8, 22.5, 19.6, 18.4, 15.8],
        [23.5, 19.4, 17.2, 16.0, 14.2]
    ]
    bc.categoryAxis.categoryNames = ['Computer Science', 'Business & Econ', 'Design & Innov', 'School of Law', 'Liberal Arts']
    bc.categoryAxis.labels.fontSize = 7
    bc.categoryAxis.labels.fontName = 'Helvetica-Bold'
    bc.categoryAxis.labels.dy = -10
    bc.valueAxis.valueMin = 0
    bc.valueAxis.valueMax = 30
    bc.valueAxis.valueStep = 5
    bc.valueAxis.labels.fontSize = 7
    bc.valueAxis.labels.fontName = 'Helvetica'
    bc.bars[0].fillColor = C_FOREST
    bc.bars[1].fillColor = C_OCHRE
    
    d_bar.add(bc)
    d_bar.add(Rect(320, 108, 10, 7, fillColor=C_FOREST, strokeColor=None))
    d_bar.add(String(335, 109, 'Average CTC (₹ LPA)', fontName='Helvetica', fontSize=7, fillColor=C_TEXT))
    d_bar.add(Rect(430, 108, 10, 7, fillColor=C_OCHRE, strokeColor=None))
    d_bar.add(String(445, 109, 'Median CTC (₹ LPA)', fontName='Helvetica', fontSize=7, fillColor=C_TEXT))
    story.append(d_bar)

    # PAGE 3: SECTOR BREAKDOWN
    story.append(PageBreak())
    story.append(Paragraph('Sector Distribution & Industry Architecture', h1))
    story.append(Paragraph('Distribution of job offers across global market segments and specialized high-demand competency clusters.', p_lead))

    d_pie = Drawing(printable_w, 145)
    d_pie.add(Rect(0, 0, printable_w, 145, fillColor=C_LIGHT, strokeColor=C_BORDER, strokeWidth=0.5, rx=3, ry=3))
    
    pie = Pie()
    pie.x = 40
    pie.y = 12
    pie.width = 120
    pie.height = 120
    pie.data = [38, 24, 18, 11, 9]
    pie.slices[0].fillColor = C_FOREST
    pie.slices[1].fillColor = C_OCHRE
    pie.slices[2].fillColor = C_SLATE
    pie.slices[3].fillColor = C_TEAL
    pie.slices[4].fillColor = C_INDIGO
    d_pie.add(pie)

    legend_items = [
        ('Technology, AI & Deep Systems (38%)', C_FOREST, 'Distributed systems, Foundation models, Cloud infra, Quant tech'),
        ('Banking, Finance & FinTech (24%)', C_OCHRE, 'Investment banking, Private equity, Quantitative modeling, Algo trading'),
        ('Strategy & Management Consulting (18%)', C_SLATE, 'Corporate transformation, Public sector advisory, M&A due diligence'),
        ('Product Innovation & Design (11%)', C_TEAL, 'Industrial design, Spatial computing, UX architecture, Design systems'),
        ('Legal Practice, Policy & Think-Tanks (9%)', C_INDIGO, 'Appellate litigation, Technology law, Climate policy, Governance')
    ]
    ly = 112
    for title, col, desc in legend_items:
        d_pie.add(Rect(185, ly, 10, 9, fillColor=col, strokeColor=None))
        d_pie.add(String(202, ly+1, title, fontName='Helvetica-Bold', fontSize=7.5, fillColor=C_TEXT))
        d_pie.add(String(202, ly-8, desc, fontName='Helvetica', fontSize=6.5, fillColor=C_MUTED))
        ly -= 23
    story.append(d_pie)
    story.append(Spacer(1, 12))

    story.append(Paragraph('Functional Competency Clusters & Compensation Profiles', h2))
    domain_data = [
        [Paragraph('Functional Domain', p_table_header), Paragraph('Key Roles Offered', p_table_header), Paragraph('Marquee Employers', p_table_header), Paragraph('Compensation Band', p_table_header)],
        [Paragraph('<b>Machine Learning & Systems</b>', p_body), Paragraph('AI Research Engineer, LLM Fine-tuning Specialist, Cloud Kernel Engineer, High-Throughput Systems Architect', p_table_cell), Paragraph('Google, Apple, Microsoft, Amazon, Atlassian', p_table_cell), Paragraph('₹32.0 – ₹64.5 LPA', p_table_cell_right_bold)],
        [Paragraph('<b>Quant Finance & Investment</b>', p_body), Paragraph('Quantitative Strategist, Fixed Income Analyst, Equity Research Associate, Risk Modeling Specialist', p_table_cell), Paragraph('Goldman Sachs, Morgan Stanley, J.P. Morgan, Mastercard', p_table_cell), Paragraph('₹28.0 – ₹44.0 LPA', p_table_cell_right_bold)],
        [Paragraph('<b>Strategy Consulting</b>', p_body), Paragraph('Management Consultant, Business Analyst, Economic Policy Fellow, Operational Transformation Associate', p_table_cell), Paragraph('McKinsey & Company, BCG, Deloitte, EY Parthenon', p_table_cell), Paragraph('₹22.0 – ₹42.0 LPA', p_table_cell_right_bold)],
        [Paragraph('<b>Product & Interaction Design</b>', p_body), Paragraph('Lead Product Designer, Design Systems Architect, Human Interface Engineer, Spatial UX Researcher', p_table_cell), Paragraph('Frog Design, IDEO, Adobe, Atlassian, Flipkart', p_table_cell), Paragraph('₹18.0 – ₹38.5 LPA', p_table_cell_right_bold)],
        [Paragraph('<b>Corporate Law & Policy</b>', p_body), Paragraph('Appellate Chambers Law Clerk, Associate Attorney (M&A/PE), Tech Regulations Counsel, Policy Researcher', p_table_cell), Paragraph('Shardul Amarchand, Trilegal, Khaitan & Co, CPR', p_table_cell), Paragraph('₹16.0 – ₹34.0 LPA', p_table_cell_right_bold)],
        [Paragraph('<b>Sustainable Tech & Mobility</b>', p_body), Paragraph('Circular Materials Engineer, EV Systems Strategist, Clean Energy Data Analyst', p_table_cell), Paragraph('Hyundai Mobility Labs, Tata Motors R&D, Schneider', p_table_cell), Paragraph('₹16.0 – ₹26.0 LPA', p_table_cell_right_bold)],
    ]
    t_domain = Table(domain_data, colWidths=[110, 163, 140, 110])
    t_domain.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), C_FOREST),
        ('BOX', (0,0), (-1,-1), 1, C_BORDER),
        ('INNERGRID', (0,0), (-1,-1), 0.5, C_BORDER),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [C_WHITE, C_LIGHT]),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(t_domain)

    # PAGE 4: RECRUITER MATRIX
    story.append(PageBreak())
    story.append(Paragraph('Corporate Recruiter Matrix & Offer Breakdown', h1))
    story.append(Paragraph('Empirical accounting of offers made by top 22 corporate partners alongside compensation ranges for the 2025–26 recruitment season.', p_lead))

    recruiter_data = [
        [Paragraph('Recruiter Organization', p_table_header), Paragraph('Sector / Domain', p_table_header), Paragraph('Offers Made', p_table_header), Paragraph('Typical CTC Range', p_table_header), Paragraph('Primary Hiring Degree Tracks', p_table_header)],
        [Paragraph('<b>Deloitte Consulting</b>', p_body), Paragraph('Management & Tech Advisory', p_table_cell), Paragraph('<b>34</b>', p_table_cell_right_bold), Paragraph('₹18.0 – ₹24.0 LPA', p_table_cell_right), Paragraph('B.Tech, B.B.A, B.Sc Economics', p_table_cell)],
        [Paragraph('<b>Tata Consultancy (Specialist R&D)</b>', p_body), Paragraph('Advanced Technology & AI', p_table_cell), Paragraph('<b>28</b>', p_table_cell_right_bold), Paragraph('₹16.0 – ₹22.0 LPA', p_table_cell_right), Paragraph('B.Tech CS, M.Sc Computing', p_table_cell)],
        [Paragraph('<b>Amazon</b>', p_body), Paragraph('Cloud Computing & E-Commerce', p_table_cell), Paragraph('<b>26</b>', p_table_cell_right_bold), Paragraph('₹40.0 – ₹46.0 LPA', p_table_cell_right), Paragraph('B.Tech CS, B.Des Interaction', p_table_cell)],
        [Paragraph('<b>Microsoft</b>', p_body), Paragraph('Enterprise Cloud & Systems', p_table_cell), Paragraph('<b>24</b>', p_table_cell_right_bold), Paragraph('₹45.0 – ₹52.0 LPA', p_table_cell_right), Paragraph('B.Tech CS, M.Sc Computing', p_table_cell)],
        [Paragraph('<b>J.P. Morgan Chase</b>', p_body), Paragraph('Investment Banking & FinTech', p_table_cell), Paragraph('<b>22</b>', p_table_cell_right_bold), Paragraph('₹30.0 – ₹36.0 LPA', p_table_cell_right), Paragraph('B.Sc Econ, B.Tech CS, B.B.A', p_table_cell)],
        [Paragraph('<b>Google</b>', p_body), Paragraph('AI Research, Systems & Search', p_table_cell), Paragraph('<b>18</b>', p_table_cell_right_bold), Paragraph('₹48.0 – ₹56.0 LPA', p_table_cell_right), Paragraph('B.Tech CS, M.Sc Computing', p_table_cell)],
        [Paragraph('<b>KPMG Strategy</b>', p_body), Paragraph('Risk, ESG & Deal Advisory', p_table_cell), Paragraph('<b>18</b>', p_table_cell_right_bold), Paragraph('₹18.0 – ₹24.0 LPA', p_table_cell_right), Paragraph('B.B.A, B.A Business & Society', p_table_cell)],
        [Paragraph('<b>Goldman Sachs</b>', p_body), Paragraph('Asset Management & Quant', p_table_cell), Paragraph('<b>16</b>', p_table_cell_right_bold), Paragraph('₹38.0 – ₹44.0 LPA', p_table_cell_right), Paragraph('B.Sc Econ, B.Tech CS', p_table_cell)],
        [Paragraph('<b>Flipkart</b>', p_body), Paragraph('Platform Tech & Supply Chain', p_table_cell), Paragraph('<b>16</b>', p_table_cell_right_bold), Paragraph('₹30.0 – ₹36.0 LPA', p_table_cell_right), Paragraph('B.Tech CS, B.Des, B.B.A', p_table_cell)],
        [Paragraph('<b>Morgan Stanley</b>', p_body), Paragraph('Institutional Securities', p_table_cell), Paragraph('<b>15</b>', p_table_cell_right_bold), Paragraph('₹32.0 – ₹38.0 LPA', p_table_cell_right), Paragraph('B.Sc Econ, B.Tech CS, B.B.A', p_table_cell)],
        [Paragraph('<b>EY Parthenon</b>', p_body), Paragraph('Strategy & Market Diligence', p_table_cell), Paragraph('<b>15</b>', p_table_cell_right_bold), Paragraph('₹22.0 – ₹28.0 LPA', p_table_cell_right), Paragraph('B.B.A, B.Sc Economics', p_table_cell)],
        [Paragraph('<b>Adobe Systems</b>', p_body), Paragraph('Creative Cloud & Document AI', p_table_cell), Paragraph('<b>14</b>', p_table_cell_right_bold), Paragraph('₹36.0 – ₹44.0 LPA', p_table_cell_right), Paragraph('B.Tech CS, B.Des IxD/Product', p_table_cell)],
        [Paragraph('<b>Frog Design & IDEO</b>', p_body), Paragraph('Human-Centered Product Design', p_table_cell), Paragraph('<b>14</b>', p_table_cell_right_bold), Paragraph('₹24.0 – ₹32.0 LPA', p_table_cell_right), Paragraph('B.Des (All Tracks), M.Des', p_table_cell)],
        [Paragraph('<b>McKinsey & Company</b>', p_body), Paragraph('Global Management Consulting', p_table_cell), Paragraph('<b>12</b>', p_table_cell_right_bold), Paragraph('₹34.0 – ₹40.0 LPA', p_table_cell_right), Paragraph('B.B.A, B.Sc Econ, B.Tech CS', p_table_cell)],
        [Paragraph('<b>Shardul Amarchand Mangaldas</b>', p_body), Paragraph('Full-Service Corporate Law', p_table_cell), Paragraph('<b>12</b>', p_table_cell_right_bold), Paragraph('₹22.0 – ₹28.0 LPA', p_table_cell_right), Paragraph('5-Yr B.A. LL.B, 3-Yr LL.B, LL.M', p_table_cell)],
        [Paragraph('<b>Mastercard</b>', p_body), Paragraph('Global Payment Networks', p_table_cell), Paragraph('<b>12</b>', p_table_cell_right_bold), Paragraph('₹28.0 – ₹34.0 LPA', p_table_cell_right), Paragraph('B.Tech CS, B.Sc Economics', p_table_cell)],
        [Paragraph('<b>Atlassian</b>', p_body), Paragraph('Developer Tools & Collaboration', p_table_cell), Paragraph('<b>11</b>', p_table_cell_right_bold), Paragraph('₹42.0 – ₹50.0 LPA', p_table_cell_right), Paragraph('B.Tech CS, B.Des IxD', p_table_cell)],
        [Paragraph('<b>Boston Consulting Group (BCG)</b>', p_body), Paragraph('Strategic Advisory', p_table_cell), Paragraph('<b>10</b>', p_table_cell_right_bold), Paragraph('₹35.0 – ₹42.0 LPA', p_table_cell_right), Paragraph('B.Sc Econ, B.B.A, B.Tech CS', p_table_cell)],
        [Paragraph('<b>Trilegal</b>', p_body), Paragraph('Corporate, Tech & Dispute Law', p_table_cell), Paragraph('<b>10</b>', p_table_cell_right_bold), Paragraph('₹20.0 – ₹26.0 LPA', p_table_cell_right), Paragraph('5-Yr B.A. LL.B, 3-Yr LL.B', p_table_cell)],
        [Paragraph('<b>Khaitan & Co</b>', p_body), Paragraph('Corporate & Banking Practice', p_table_cell), Paragraph('<b>9</b>', p_table_cell_right_bold), Paragraph('₹21.0 – ₹27.0 LPA', p_table_cell_right), Paragraph('5-Yr B.A. LL.B, LL.M', p_table_cell)],
        [Paragraph('<b>Apple</b>', p_body), Paragraph('Silicon, OS & Neural Tech', p_table_cell), Paragraph('<b>8</b>', p_table_cell_right_bold), Paragraph('₹54.0 – ₹64.5 LPA', p_table_cell_right), Paragraph('B.Tech CS (Hardware/ML)', p_table_cell)],
        [Paragraph('<b>Hyundai Mobility Labs</b>', p_body), Paragraph('Autonomous & Electric Mobility', p_table_cell), Paragraph('<b>8</b>', p_table_cell_right_bold), Paragraph('₹20.0 – ₹26.0 LPA', p_table_cell_right), Paragraph('B.Tech CS, B.Des Product', p_table_cell)],
        [Paragraph('<b>Top 22 Recruiters Total</b>', p_body), Paragraph('Premier Marquee Tiers', p_table_cell), Paragraph('<b>382</b>', p_table_cell_right_bold), Paragraph('₹28.4 LPA (Tier Avg)', p_table_cell_right_bold), Paragraph('All Disciplines Represented', p_table_cell_bold)],
    ]
    t_recruiter = Table(recruiter_data, colWidths=[120, 115, 52, 95, 141])
    t_recruiter.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), C_FOREST),
        ('BOX', (0,0), (-1,-1), 1, C_BORDER),
        ('INNERGRID', (0,0), (-1,-1), 0.5, C_BORDER),
        ('ROWBACKGROUNDS', (0,1), (-1,-2), [C_WHITE, C_LIGHT]),
        ('BACKGROUND', (0,-1), (-1,-1), HexColor('#e6f0eb')),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
    ]))
    story.append(t_recruiter)
    story.append(Spacer(1, 6))
    story.append(Paragraph('<i>Note: 1,100 additional offers were extended by 360+ other recruiting partners, including global technology unicorns, sovereign research councils, boutique consulting firms, and public interest organizations.</i>', p_body))

    # PAGE 5: STUDENT PLACEMENT ROLL OF HONOUR
    story.append(PageBreak())
    story.append(Paragraph('Student Placement Roll of Honour', h1))
    story.append(Paragraph('Celebrating individual student achievements and career milestones across our multidisciplinary graduating cohort.', p_lead))

    student_data = [
        [Paragraph('Student Name', p_table_header), Paragraph('Degree & Major', p_table_header), Paragraph('Hiring Partner', p_table_header), Paragraph('Designation / Role', p_table_header), Paragraph('CTC Package', p_table_header), Paragraph('Location', p_table_header)],
        [Paragraph('<b>Meera Krishnan</b>', p_body), Paragraph('B.Tech. Computer Science', p_table_cell), Paragraph('<b>Apple Inc.</b>', p_table_cell_bold), Paragraph('Silicon & Neural Engine Engineer', p_table_cell), Paragraph('<b>₹64.50 LPA</b>', p_table_cell_right_bold), Paragraph('Hyderabad / Cupertino', p_table_cell)],
        [Paragraph('<b>Aarav Sharma</b>', p_body), Paragraph('B.Tech. Computer Science', p_table_cell), Paragraph('<b>Google</b>', p_table_cell_bold), Paragraph('Machine Learning Research Engineer', p_table_cell), Paragraph('<b>₹56.00 LPA</b>', p_table_cell_right_bold), Paragraph('Bengaluru', p_table_cell)],
        [Paragraph('<b>Siddharth Nair</b>', p_body), Paragraph('M.Sc. Advanced Computing', p_table_cell), Paragraph('<b>Microsoft</b>', p_table_cell_bold), Paragraph('Distributed Systems Architect', p_table_cell), Paragraph('<b>₹52.00 LPA</b>', p_table_cell_right_bold), Paragraph('Hyderabad', p_table_cell)],
        [Paragraph('<b>Diya Nambiar</b>', p_body), Paragraph('B.Des. Interaction Design', p_table_cell), Paragraph('<b>Atlassian</b>', p_table_cell_bold), Paragraph('Design Systems UX Lead', p_table_cell), Paragraph('<b>₹46.00 LPA</b>', p_table_cell_right_bold), Paragraph('Bengaluru', p_table_cell)],
        [Paragraph('<b>Ishaan Bhatia</b>', p_body), Paragraph('B.Tech. Computer Science', p_table_cell), Paragraph('<b>Amazon</b>', p_table_cell_bold), Paragraph('AWS Cloud Kernel Developer', p_table_cell), Paragraph('<b>₹45.00 LPA</b>', p_table_cell_right_bold), Paragraph('Bengaluru', p_table_cell)],
        [Paragraph('<b>Tanishq Mehra</b>', p_body), Paragraph('B.Sc. in Economics', p_table_cell), Paragraph('<b>Goldman Sachs</b>', p_table_cell_bold), Paragraph('Quantitative Strategies Analyst', p_table_cell), Paragraph('<b>₹44.00 LPA</b>', p_table_cell_right_bold), Paragraph('Bengaluru / London', p_table_cell)],
        [Paragraph('<b>Pranav Kulkarni</b>', p_body), Paragraph('B.Sc. in Economics', p_table_cell), Paragraph('<b>Boston Consulting Group</b>', p_table_cell_bold), Paragraph('Management Consultant', p_table_cell), Paragraph('<b>₹42.00 LPA</b>', p_table_cell_right_bold), Paragraph('Gurugram', p_table_cell)],
        [Paragraph('<b>Kabir Sen</b>', p_body), Paragraph('B.B.A. Management', p_table_cell), Paragraph('<b>McKinsey & Company</b>', p_table_cell_bold), Paragraph('Junior Associate Consultant', p_table_cell), Paragraph('<b>₹40.00 LPA</b>', p_table_cell_right_bold), Paragraph('Mumbai', p_table_cell)],
        [Paragraph('<b>Shreya Vasudev</b>', p_body), Paragraph('B.Tech. Computer Science', p_table_cell), Paragraph('<b>Adobe Systems</b>', p_table_cell_bold), Paragraph('Computer Vision Engineer', p_table_cell), Paragraph('<b>₹38.00 LPA</b>', p_table_cell_right_bold), Paragraph('Noida', p_table_cell)],
        [Paragraph('<b>Nikhil Agarwal</b>', p_body), Paragraph('M.Sc. in Economics', p_table_cell), Paragraph('<b>Morgan Stanley</b>', p_table_cell_bold), Paragraph('Fixed Income Macro Analyst', p_table_cell), Paragraph('<b>₹36.00 LPA</b>', p_table_cell_right_bold), Paragraph('Mumbai', p_table_cell)],
        [Paragraph('<b>Ananya Sengupta</b>', p_body), Paragraph('B.Des. Product Design', p_table_cell), Paragraph('<b>Frog Design</b>', p_table_cell_bold), Paragraph('Industrial Innovation Designer', p_table_cell), Paragraph('<b>₹32.00 LPA</b>', p_table_cell_right_bold), Paragraph('Bengaluru', p_table_cell)],
        [Paragraph('<b>Rhea Deshmukh</b>', p_body), Paragraph('5-Year B.A. LL.B. (Hons.)', p_table_cell), Paragraph('<b>Shardul Amarchand</b>', p_table_cell_bold), Paragraph('Associate, Tech & M&A Practice', p_table_cell), Paragraph('<b>₹28.00 LPA</b>', p_table_cell_right_bold), Paragraph('New Delhi', p_table_cell)],
        [Paragraph('<b>Devika Menon</b>', p_body), Paragraph('3-Year LL.B. (Hons.)', p_table_cell), Paragraph('<b>Trilegal</b>', p_table_cell_bold), Paragraph('Associate, Corporate Arbitration', p_table_cell), Paragraph('<b>₹26.00 LPA</b>', p_table_cell_right_bold), Paragraph('Mumbai', p_table_cell)],
        [Paragraph('<b>Tanvi Joshi</b>', p_body), Paragraph('B.A. (Hons.) Liberal Arts', p_table_cell), Paragraph('<b>Centre for Policy Research</b>', p_table_cell_bold), Paragraph('Lead Climate Policy Fellow', p_table_cell), Paragraph('<b>₹24.00 LPA</b>', p_table_cell_right_bold), Paragraph('New Delhi', p_table_cell)],
        [Paragraph('<b>Varun Patel</b>', p_body), Paragraph('B.A. Business & Society', p_table_cell), Paragraph('<b>Deloitte Consulting</b>', p_table_cell_bold), Paragraph('ESG Strategy & Risk Analyst', p_table_cell), Paragraph('<b>₹22.00 LPA</b>', p_table_cell_right_bold), Paragraph('Hyderabad', p_table_cell)],
        [Paragraph('<b>Kavya Sundaram</b>', p_body), Paragraph('LL.M. Postgraduate Law', p_table_cell), Paragraph('<b>Khaitan & Co</b>', p_table_cell_bold), Paragraph('Senior Associate, Competition Law', p_table_cell), Paragraph('<b>₹27.00 LPA</b>', p_table_cell_right_bold), Paragraph('Bengaluru', p_table_cell)],
    ]
    t_student = Table(student_data, colWidths=[90, 105, 105, 115, 58, 50])
    t_student.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), C_FOREST),
        ('BOX', (0,0), (-1,-1), 1, C_BORDER),
        ('INNERGRID', (0,0), (-1,-1), 0.5, C_BORDER),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [C_WHITE, C_LIGHT]),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
    ]))
    story.append(t_student)

    # PAGE 6: SUMMER INTERNSHIPS, PPOS & GLOBAL HUBS
    story.append(PageBreak())
    story.append(Paragraph('Summer Internships, PPOs & Global Placements', h1))
    story.append(Paragraph('Bridging experiential academic learning with world-class corporate apprenticeships and international employment hubs.', p_lead))

    intern_metrics = [
        [
            Paragraph('<b><font size="12" color="#1b3d2f">850+</font></b><br/><font size="6.5" color="#64748b">Funded Summer Internships</font>', p_body),
            Paragraph('<b><font size="12" color="#1b3d2f">₹1.45 Lakh/mo</font></b><br/><font size="6.5" color="#64748b">Highest Internship Stipend</font>', p_body),
            Paragraph('<b><font size="12" color="#1b3d2f">₹58,000/mo</font></b><br/><font size="6.5" color="#64748b">Average Internship Stipend</font>', p_body),
            Paragraph('<b><font size="12" color="#c59b27">74%</font></b><br/><font size="6.5" color="#64748b">Internship to PPO Conversion</font>', p_body),
        ]
    ]
    t_in_metrics = Table(intern_metrics, colWidths=[printable_w/4.0]*4)
    t_in_metrics.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), C_LIGHT),
        ('BOX', (0,0), (-1,-1), 1, C_BORDER),
        ('INNERGRID', (0,0), (-1,-1), 0.5, C_BORDER),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(t_in_metrics)
    story.append(Spacer(1, 12))

    story.append(Paragraph('Global Recruitment Locations (International Placements)', h2))
    intl_sf = '$165,000 (₹1.38 Cr)'
    global_loc_data = [
        [Paragraph('Global Region / City', p_table_header), Paragraph('Participating Employers', p_table_header), Paragraph('Roles Offered', p_table_header), Paragraph('Highest International CTC', p_table_header)],
        [Paragraph('<b>San Francisco Bay Area, USA</b>', p_body), Paragraph('Silicon Valley Big Tech, AI Research Labs', p_table_cell), Paragraph('AI Research Scientist, Systems Engineer', p_table_cell), Paragraph(intl_sf, p_table_cell_right_bold)],
        [Paragraph('<b>London, United Kingdom</b>', p_body), Paragraph('Global Investment Banks, Magic Circle Law', p_table_cell), Paragraph('Quant Trader, Cross-Border M&A Associate', p_table_cell), Paragraph('£95,000 (₹1.02 Cr)', p_table_cell_right_bold)],
        [Paragraph('<b>Zurich, Switzerland</b>', p_body), Paragraph('European Tech Hubs & Wealth Management', p_table_cell), Paragraph('Computer Vision Lead, Quantitative Analyst', p_table_cell), Paragraph('CHF 120,000 (₹1.15 Cr)', p_table_cell_right_bold)],
        [Paragraph('<b>Singapore</b>', p_body), Paragraph('FinTech Unicorns, Regional Headquarters', p_table_cell), Paragraph('Product Lead, Algorithmic Execution Engineer', p_table_cell), Paragraph('SGD 115,000 (₹72 LPA)', p_table_cell_right_bold)],
        [Paragraph('<b>Tokyo, Japan</b>', p_body), Paragraph('Robotics Labs, Advanced Manufacturing', p_table_cell), Paragraph('Mechatronics Specialist, Industrial Designer', p_table_cell), Paragraph('JPY 9,500,000 (₹54 LPA)', p_table_cell_right_bold)],
    ]
    t_global = Table(global_loc_data, colWidths=[125, 140, 148, 110])
    t_global.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), C_FOREST),
        ('BOX', (0,0), (-1,-1), 1, C_BORDER),
        ('INNERGRID', (0,0), (-1,-1), 0.5, C_BORDER),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [C_WHITE, C_LIGHT]),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(t_global)
    story.append(Spacer(1, 12))

    protocol_text = '''<b>Corporate Relations & Recruitment Protocol:</b><br/>
    Aaranya University invites distinguished corporate partners, statutory agencies, and non-profit enterprises to participate in our annual recruitment process. Our placement cycle proceeds across structured phases:
    <br/><br/>
    • <b>Phase 1 (Pre-Placement Talks & Hackathons):</b> July – August (On-campus workshops, hackathons at The Crucible, and executive keynote talks).<br/>
    • <b>Phase 2 (Summer Internship Assessments & PPOs):</b> September – October (Pre-Placement Offer confirmations for returning interns).<br/>
    • <b>Phase 3 (Marquee & Day 0 Placements):</b> November – December (Marquee engineering, investment banking, consulting, and appellate law interviews).<br/>
    • <b>Phase 4 (Rolling Placement Drives):</b> January – April (Continuous engagement across startups, public interest fellows, and multidisciplinary roles).
    <br/><br/>
    <b>Corporate Relations Office:</b> The Forum, Landmark Building #10, Aaranya University Campus, Lakeside Parkway, Green Hills.<br/>
    <b>Direct Line:</b> +91 (0) 800-AARANYA-CAREERS / +91 80 4567 8900 · <b>Email:</b> placements@aaranya.edu.in · <b>Web:</b> https://aaranya.edu.in/placements.html'''
    
    t_proto = Table([[Paragraph(protocol_text, p_body)]], colWidths=[printable_w])
    t_proto.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), HexColor('#f8fafc')),
        ('BOX', (0,0), (-1,-1), 1, HexColor('#cbd5e1')),
        ('LINELEFT', (0,0), (0,-1), 4, C_OCHRE),
        ('TOPPADDING', (0,0), (-1,-1), 8),
        ('BOTTOMPADDING', (0,0), (-1,-1), 8),
        ('LEFTPADDING', (0,0), (-1,-1), 11),
        ('RIGHTPADDING', (0,0), (-1,-1), 11),
    ]))
    story.append(t_proto)

    doc.build(story, canvasmaker=NumberedCanvas)
    print(f'PDF Brochure created successfully at: {output_path} ({os.path.getsize(output_path)} bytes)')

if __name__ == '__main__':
    out_file = os.path.join(workspace_dir, 'assets', 'docs', 'Aaranya_University_Placement_Report_2025-26.pdf')
    create_brochure_pdf(out_file)
