import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE
from pptx.dml.color import RGBColor

# -----------------------------------------------------------------------------
# Color Palette Definitions (Dark Navy, White, Subtle Teal)
# -----------------------------------------------------------------------------
COLOR_DARK_NAVY = RGBColor(15, 23, 42)      # #0F172A - Slate 900
COLOR_HEADER_NAVY = RGBColor(30, 41, 59)    # #1E293B - Slate 800
COLOR_TEAL_PRIMARY = RGBColor(13, 148, 136) # #0D9488 - Teal 600
COLOR_TEAL_LIGHT = RGBColor(20, 184, 166)   # #14B8A6 - Teal 500
COLOR_TEAL_BG = RGBColor(240, 253, 250)     # #F0FDF4 - Light teal tint
COLOR_BG_LIGHT = RGBColor(248, 250, 252)    # #F8FAFC - Background light
COLOR_CARD_BG = RGBColor(255, 255, 255)     # #FFFFFF - Pure white
COLOR_BORDER = RGBColor(226, 232, 240)      # #E2E8F0 - Border gray
COLOR_TEXT_MAIN = RGBColor(15, 23, 42)      # #0F172A - Main dark text
COLOR_TEXT_MUTED = RGBColor(100, 116, 139)  # #64748B - Muted text gray
COLOR_WHITE = RGBColor(255, 255, 255)

# Module specific accent colors from UIUtils.java
COLOR_M1_BLUE = RGBColor(37, 99, 235)      # M1 - Pattern Matching
COLOR_M2_CYAN = RGBColor(6, 182, 212)      # M2 - Document Similarity
COLOR_M3_EMERALD = RGBColor(16, 185, 129)  # M3 - Optimization & Distance
COLOR_M4_PURPLE = RGBColor(147, 51, 234)   # M4 - Resource Allocation
COLOR_M5_AMBER = RGBColor(245, 158, 11)    # M5 - Conflict Management
COLOR_M6_ROSE = RGBColor(244, 63, 94)      # M6 - Event Analytics

FONT_FAMILY = "Segoe UI"

def create_presentation():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]  # Blank layout

    def set_background(slide, color):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
        bg.fill.solid()
        bg.fill.fore_color.rgb = color
        bg.line.fill.background()
        return bg

    def add_header(slide, title_text, category_tag):
        hdr_bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, Inches(1.1))
        hdr_bar.fill.solid()
        hdr_bar.fill.fore_color.rgb = COLOR_DARK_NAVY
        hdr_bar.line.fill.background()

        tag_shape = slide.shapes.add_shape(
            MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(0.18), Inches(3.4), Inches(0.3)
        )
        tag_shape.fill.solid()
        tag_shape.fill.fore_color.rgb = COLOR_TEAL_PRIMARY
        tag_shape.line.fill.background()
        tf_tag = tag_shape.text_frame
        tf_tag.word_wrap = True
        tf_tag.margin_left = tf_tag.margin_right = tf_tag.margin_top = tf_tag.margin_bottom = 0
        p_tag = tf_tag.paragraphs[0]
        p_tag.text = category_tag.upper()
        p_tag.font.name = FONT_FAMILY
        p_tag.font.size = Pt(10)
        p_tag.font.bold = True
        p_tag.font.color.rgb = COLOR_WHITE
        p_tag.alignment = PP_ALIGN.CENTER

        tx_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.48), Inches(11.5), Inches(0.5))
        tf = tx_box.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
        p = tf.paragraphs[0]
        p.text = title_text
        p.font.name = FONT_FAMILY
        p.font.size = Pt(22)
        p.font.bold = True
        p.font.color.rgb = COLOR_WHITE

        accent = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, Inches(1.08), prs.slide_width, Inches(0.04))
        accent.fill.solid()
        accent.fill.fore_color.rgb = COLOR_TEAL_LIGHT
        accent.line.fill.background()

        ftr_box = slide.shapes.add_textbox(Inches(0.8), Inches(7.15), Inches(11.733), Inches(0.3))
        tf_ftr = ftr_box.text_frame
        p_ftr = tf_ftr.paragraphs[0]
        p_ftr.text = "EventFlow — College Event Management Platform  |  Java Swing & DSA Project Review"
        p_ftr.font.name = FONT_FAMILY
        p_ftr.font.size = Pt(10)
        p_ftr.font.color.rgb = COLOR_TEXT_MUTED

    def add_card(slide, left, top, width, height, bg_color=COLOR_CARD_BG, border_color=COLOR_BORDER, accent_top=None):
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = bg_color
        if border_color:
            card.line.color.rgb = border_color
            card.line.width = Pt(1)
        else:
            card.line.fill.background()

        if accent_top:
            acc = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, left, top, width, Inches(0.08))
            acc.fill.solid()
            acc.fill.fore_color.rgb = accent_top
            acc.line.fill.background()

        return card

    # =========================================================================
    # SLIDE 1: Title Slide
    # =========================================================================
    slide1 = prs.slides.add_slide(blank_layout)
    set_background(slide1, COLOR_DARK_NAVY)

    top_dec = slide1.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, Inches(0.12))
    top_dec.fill.solid()
    top_dec.fill.fore_color.rgb = COLOR_TEAL_LIGHT
    top_dec.line.fill.background()

    badge = slide1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.0), Inches(1.1), Inches(4.2), Inches(0.38))
    badge.fill.solid()
    badge.fill.fore_color.rgb = COLOR_TEAL_PRIMARY
    badge.line.fill.background()
    p_b = badge.text_frame.paragraphs[0]
    p_b.text = "COLLEGE EVENT MANAGEMENT PLATFORM"
    p_b.font.name = FONT_FAMILY
    p_b.font.size = Pt(11)
    p_b.font.bold = True
    p_b.font.color.rgb = COLOR_WHITE
    p_b.alignment = PP_ALIGN.CENTER

    tbox = slide1.shapes.add_textbox(Inches(1.0), Inches(1.6), Inches(11.0), Inches(1.2))
    tf1 = tbox.text_frame
    tf1.word_wrap = True
    p1 = tf1.paragraphs[0]
    p1.text = "EventFlow"
    p1.font.name = FONT_FAMILY
    p1.font.size = Pt(54)
    p1.font.bold = True
    p1.font.color.rgb = COLOR_WHITE

    p1_sub = tf1.add_paragraph()
    p1_sub.text = "Built using Java Swing and Data Structures & Algorithms"
    p1_sub.font.name = FONT_FAMILY
    p1_sub.font.size = Pt(20)
    p1_sub.font.color.rgb = COLOR_TEAL_LIGHT
    p1_sub.space_before = Pt(8)

    p1_desc = tf1.add_paragraph()
    p1_desc.text = "A modular desktop application for centralized event administration, resource allocation, and conflict management."
    p1_desc.font.name = FONT_FAMILY
    p1_desc.font.size = Pt(13)
    p1_desc.font.color.rgb = COLOR_TEXT_MUTED
    p1_desc.space_before = Pt(10)

    meta_top = Inches(4.5)
    card_width = Inches(2.65)
    card_height = Inches(1.9)
    spacing = Inches(0.24)

    meta_items = [
        ("STUDENT NAME", "[Student Name]"),
        ("ROLL NUMBER", "[Roll Number]"),
        ("DEPARTMENT", "[Department Name]"),
        ("PROJECT GUIDE", "[Guide Name]")
    ]

    for idx, (label, val) in enumerate(meta_items):
        left_pos = Inches(1.0) + idx * (card_width + spacing)
        c_shape = slide1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left_pos, meta_top, card_width, card_height)
        c_shape.fill.solid()
        c_shape.fill.fore_color.rgb = COLOR_HEADER_NAVY
        c_shape.line.color.rgb = COLOR_TEAL_PRIMARY
        c_shape.line.width = Pt(1)

        acc = slide1.shapes.add_shape(MSO_SHAPE.RECTANGLE, left_pos, meta_top, card_width, Inches(0.06))
        acc.fill.solid()
        acc.fill.fore_color.rgb = COLOR_TEAL_LIGHT
        acc.line.fill.background()

        tf_m = c_shape.text_frame
        tf_m.word_wrap = True
        tf_m.margin_left = Inches(0.18)
        tf_m.margin_top = Inches(0.25)
        tf_m.margin_right = Inches(0.18)

        p_lbl = tf_m.paragraphs[0]
        p_lbl.text = label
        p_lbl.font.name = FONT_FAMILY
        p_lbl.font.size = Pt(10)
        p_lbl.font.bold = True
        p_lbl.font.color.rgb = COLOR_TEAL_LIGHT

        p_val = tf_m.add_paragraph()
        p_val.text = val
        p_val.font.name = FONT_FAMILY
        p_val.font.size = Pt(14)
        p_val.font.bold = True
        p_val.font.color.rgb = COLOR_WHITE
        p_val.space_before = Pt(12)

    # =========================================================================
    # SLIDE 2: Problem Statement
    # =========================================================================
    slide2 = prs.slides.add_slide(blank_layout)
    set_background(slide2, COLOR_BG_LIGHT)
    add_header(slide2, "Problem Statement", "Challenges in College Event Management")

    prob_cards = [
        (
            "Manual Administration & Fragmented Data",
            "Fragmented Management",
            [
                "Managing events, participants, venues, and student volunteers manually leads to data inconsistency.",
                "Lack of a centralized real-time dashboard creates communication gaps and tracking errors across departments."
            ]
        ),
        (
            "Search & Information Retrieval Inefficiencies",
            "Retrieval Inefficiencies",
            [
                "Searching through hundreds of registration records and log files causes computational delay.",
                "Basic text lookups fail to support substring pattern matching and document similarity evaluations."
            ]
        ),
        (
            "Resource Allocation & Scheduling Conflicts",
            "Operational Bottlenecks",
            [
                "Allocating auditoriums, labs, and equipment without automated scheduling leads to frequent venue overlaps.",
                "Manual volunteer mapping and schedule validation fail to detect multi-variable conflicts efficiently."
            ]
        )
    ]

    c_w = Inches(3.64)
    c_h = Inches(4.3)
    c_y = Inches(1.5)
    c_sp = Inches(0.4)

    for i, (title, sub, bullets) in enumerate(prob_cards):
        c_x = Inches(0.8) + i * (c_w + c_sp)
        add_card(slide2, c_x, c_y, c_w, c_h, accent_top=COLOR_TEAL_PRIMARY)

        tx = slide2.shapes.add_textbox(c_x + Inches(0.2), c_y + Inches(0.25), c_w - Inches(0.4), c_h - Inches(0.5))
        tf = tx.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0

        p_t = tf.paragraphs[0]
        p_t.text = title
        p_t.font.name = FONT_FAMILY
        p_t.font.size = Pt(16)
        p_t.font.bold = True
        p_t.font.color.rgb = COLOR_TEXT_MAIN

        p_s = tf.add_paragraph()
        p_s.text = sub.upper()
        p_s.font.name = FONT_FAMILY
        p_s.font.size = Pt(10)
        p_s.font.bold = True
        p_s.font.color.rgb = COLOR_TEAL_PRIMARY
        p_s.space_before = Pt(4)

        for b in bullets:
            p_b = tf.add_paragraph()
            p_b.text = "• " + b
            p_b.font.name = FONT_FAMILY
            p_b.font.size = Pt(12)
            p_b.font.color.rgb = COLOR_TEXT_MUTED
            p_b.space_before = Pt(12)

    add_card(slide2, Inches(0.8), Inches(6.0), Inches(11.733), Inches(0.85), bg_color=COLOR_DARK_NAVY, border_color=None)
    tx_bot = slide2.shapes.add_textbox(Inches(1.0), Inches(6.1), Inches(11.333), Inches(0.65))
    tf_bot = tx_bot.text_frame
    tf_bot.word_wrap = True
    p_b0 = tf_bot.paragraphs[0]
    p_b0.text = "CORE REQUIREMENT: A unified platform combining interactive administrative management with custom Data Structures & Algorithms for real-time searching, optimization, and conflict resolution."
    p_b0.font.name = FONT_FAMILY
    p_b0.font.size = Pt(12)
    p_b0.font.bold = True
    p_b0.font.color.rgb = COLOR_WHITE

    # =========================================================================
    # SLIDE 3: Proposed Solution
    # =========================================================================
    slide3 = prs.slides.add_slide(blank_layout)
    set_background(slide3, COLOR_BG_LIGHT)
    add_header(slide3, "Proposed Solution", "The EventFlow Management Architecture")

    c1_x = Inches(0.8)
    c1_y = Inches(1.5)
    col_w = Inches(5.66)
    col_h = Inches(5.35)

    add_card(slide3, c1_x, c1_y, col_w, col_h, accent_top=COLOR_DARK_NAVY)

    tx_col1 = slide3.shapes.add_textbox(c1_x + Inches(0.25), c1_y + Inches(0.25), col_w - Inches(0.5), col_h - Inches(0.5))
    tf_c1 = tx_col1.text_frame
    tf_c1.word_wrap = True

    p_h1 = tf_c1.paragraphs[0]
    p_h1.text = "1. Core Administrative Modules"
    p_h1.font.name = FONT_FAMILY
    p_h1.font.size = Pt(18)
    p_h1.font.bold = True
    p_h1.font.color.rgb = COLOR_TEXT_MAIN

    p_sub1 = tf_c1.add_paragraph()
    p_sub1.text = "Organizes event-related information cleanly across 4 core panels:"
    p_sub1.font.name = FONT_FAMILY
    p_sub1.font.size = Pt(11)
    p_sub1.font.color.rgb = COLOR_TEAL_PRIMARY
    p_sub1.space_before = Pt(4)

    m_items = [
        ("Dashboard Panel", "Displays real-time metric statistics (Total Events, Registrations, Active Statuses) and live event directory."),
        ("Event Directory", "Centralized hub for managing event records, schedule dates, registration limits, and category filters."),
        ("Participant Registry", "Manages student registration records, department affiliations, and participant contact details."),
        ("Venue Manager", "Tracks auditorium and lab seating capacities, locations, and booking availability across campus.")
    ]

    for title, desc in m_items:
        p_t = tf_c1.add_paragraph()
        p_t.text = "• " + title
        p_t.font.name = FONT_FAMILY
        p_t.font.size = Pt(13)
        p_t.font.bold = True
        p_t.font.color.rgb = COLOR_TEXT_MAIN
        p_t.space_before = Pt(10)

        p_d = tf_c1.add_paragraph()
        p_d.text = desc
        p_d.font.name = FONT_FAMILY
        p_d.font.size = Pt(11)
        p_d.font.color.rgb = COLOR_TEXT_MUTED
        p_d.space_before = Pt(2)

    c2_x = Inches(6.87)
    add_card(slide3, c2_x, c1_y, col_w, col_h, accent_top=COLOR_TEAL_PRIMARY)

    tx_col2 = slide3.shapes.add_textbox(c2_x + Inches(0.25), c1_y + Inches(0.25), col_w - Inches(0.5), col_h - Inches(0.5))
    tf_c2 = tx_col2.text_frame
    tf_c2.word_wrap = True

    p_h2 = tf_c2.paragraphs[0]
    p_h2.text = "2. DSA Algorithmic Processing Engine"
    p_h2.font.name = FONT_FAMILY
    p_h2.font.size = Pt(18)
    p_h2.font.bold = True
    p_h2.font.color.rgb = COLOR_TEXT_MAIN

    p_sub2 = tf_c2.add_paragraph()
    p_sub2.text = "Supports administrative operations with specialized DSA algorithms:"
    p_sub2.font.name = FONT_FAMILY
    p_sub2.font.size = Pt(11)
    p_sub2.font.color.rgb = COLOR_TEAL_PRIMARY
    p_sub2.space_before = Pt(4)

    dsa_items = [
        ("High-Performance Pattern Matching", "Executes KMP exact matching and Rabin-Karp rolling hashes to locate search terms instantenously."),
        ("Activity Optimization & Distance", "Uses Bitmask Dynamic Programming for sub-event scheduling and Levenshtein Distance for fuzzy string matching."),
        ("Resource & Volunteer Allocation", "Applies Dinic's Maximum Flow and Bipartite Graph Matching to allocate volunteers and equipment efficiently."),
        ("Conflict Management & Analytics", "Utilizes 3-SAT logic and Vertex Cover Approximation to detect schedule overlaps and compute minimal monitor nodes.")
    ]

    for title, desc in dsa_items:
        p_t = tf_c2.add_paragraph()
        p_t.text = "• " + title
        p_t.font.name = FONT_FAMILY
        p_t.font.size = Pt(13)
        p_t.font.bold = True
        p_t.font.color.rgb = COLOR_TEXT_MAIN
        p_t.space_before = Pt(10)

        p_d = tf_c2.add_paragraph()
        p_d.text = desc
        p_d.font.name = FONT_FAMILY
        p_d.font.size = Pt(11)
        p_d.font.color.rgb = COLOR_TEXT_MUTED
        p_d.space_before = Pt(2)

    # =========================================================================
    # SLIDE 4: System Architecture (With Visual Flow Connectors)
    # =========================================================================
    slide4 = prs.slides.add_slide(blank_layout)
    set_background(slide4, COLOR_BG_LIGHT)
    add_header(slide4, "System Architecture", "Source Code Component Diagram & Data Flow")

    # Entry Point Box (Top Layer)
    ep = add_card(slide4, Inches(4.66), Inches(1.35), Inches(4.0), Inches(0.55), bg_color=COLOR_DARK_NAVY, border_color=None)
    tf_ep = ep.text_frame
    p_ep = tf_ep.paragraphs[0]
    p_ep.text = "Application Entry Point (Main.java)"
    p_ep.font.name = FONT_FAMILY
    p_ep.font.size = Pt(12)
    p_ep.font.bold = True
    p_ep.font.color.rgb = COLOR_WHITE
    p_ep.alignment = PP_ALIGN.CENTER

    # Down Arrow 1
    arr1 = slide4.shapes.add_shape(MSO_SHAPE.DOWN_ARROW, Inches(6.46), Inches(1.92), Inches(0.4), Inches(0.25))
    arr1.fill.solid()
    arr1.fill.fore_color.rgb = COLOR_TEAL_PRIMARY
    arr1.line.fill.background()

    # Swing Controller Box (Layer 2)
    sf = add_card(slide4, Inches(3.66), Inches(2.2), Inches(6.0), Inches(0.6), bg_color=COLOR_TEAL_PRIMARY, border_color=None)
    tf_sf = sf.text_frame
    p_sf = tf_sf.paragraphs[0]
    p_sf.text = "Java Swing UI Window & Navigation Controller (MainFrame.java / UIUtils.java)"
    p_sf.font.name = FONT_FAMILY
    p_sf.font.size = Pt(12)
    p_sf.font.bold = True
    p_sf.font.color.rgb = COLOR_WHITE
    p_sf.alignment = PP_ALIGN.CENTER

    # Down Arrow 2
    arr2 = slide4.shapes.add_shape(MSO_SHAPE.DOWN_ARROW, Inches(6.46), Inches(2.83), Inches(0.4), Inches(0.25))
    arr2.fill.solid()
    arr2.fill.fore_color.rgb = COLOR_TEAL_PRIMARY
    arr2.line.fill.background()

    # Management Panels Container (Layer 3 - Left)
    mp = add_card(slide4, Inches(0.8), Inches(3.12), Inches(5.66), Inches(1.5), accent_top=COLOR_HEADER_NAVY)
    tf_mp = mp.text_frame
    tf_mp.word_wrap = True
    tf_mp.margin_left = tf_mp.margin_right = Inches(0.2)
    tf_mp.margin_top = Inches(0.1)
    p_mp1 = tf_mp.paragraphs[0]
    p_mp1.text = "Management View Panels"
    p_mp1.font.name = FONT_FAMILY
    p_mp1.font.size = Pt(13)
    p_mp1.font.bold = True
    p_mp1.font.color.rgb = COLOR_TEXT_MAIN

    p_mp2 = tf_mp.add_paragraph()
    p_mp2.text = "• DashboardPanel (System overview metrics & active events)\n• EventPanel (Event directory & category filter controls)\n• ParticipantPanel (Student registrations table & search)\n• VenuePanel (Auditorium & laboratory capacity directory)"
    p_mp2.font.name = FONT_FAMILY
    p_mp2.font.size = Pt(9.5)
    p_mp2.font.color.rgb = COLOR_TEXT_MUTED
    p_mp2.space_before = Pt(3)

    # DSA Processing Panels Container (Layer 3 - Right)
    dp = add_card(slide4, Inches(6.87), Inches(3.12), Inches(5.66), Inches(1.5), accent_top=COLOR_TEAL_PRIMARY)
    tf_dp = dp.text_frame
    tf_dp.word_wrap = True
    tf_dp.margin_left = tf_dp.margin_right = Inches(0.2)
    tf_dp.margin_top = Inches(0.1)
    p_dp1 = tf_dp.paragraphs[0]
    p_dp1.text = "Six DSA Module Processing Panels"
    p_dp1.font.name = FONT_FAMILY
    p_dp1.font.size = Pt(13)
    p_dp1.font.bold = True
    p_dp1.font.color.rgb = COLOR_TEXT_MAIN

    p_dp2 = tf_dp.add_paragraph()
    p_dp2.text = "• M1SearchPanel (KMP & Rabin-Karp String Search UI)\n• M2DocumentPanel (Suffix Array & LCP Similarity UI)\n• M3OptimizationPanel (Bitmask DP & Distance UI)\n• M4ResourcePanel & M5ConflictPanel & M6AnalyticsPanel UI"
    p_dp2.font.name = FONT_FAMILY
    p_dp2.font.size = Pt(9.5)
    p_dp2.font.color.rgb = COLOR_TEXT_MUTED
    p_dp2.space_before = Pt(3)

    # Down Arrow 3
    arr3 = slide4.shapes.add_shape(MSO_SHAPE.DOWN_ARROW, Inches(6.46), Inches(4.65), Inches(0.4), Inches(0.22))
    arr3.fill.solid()
    arr3.fill.fore_color.rgb = COLOR_TEAL_PRIMARY
    arr3.line.fill.background()

    # DSA Algorithm Packages Layer (Layer 4)
    algo_card = add_card(slide4, Inches(0.8), Inches(4.9), Inches(11.733), Inches(0.9), accent_top=COLOR_TEAL_LIGHT)
    tf_alg = algo_card.text_frame
    tf_alg.word_wrap = True
    tf_alg.margin_left = tf_alg.margin_right = Inches(0.2)
    tf_alg.margin_top = Inches(0.1)
    p_a1 = tf_alg.paragraphs[0]
    p_a1.text = "Algorithmic Core Execution Layer (src/algorithms/)"
    p_a1.font.name = FONT_FAMILY
    p_a1.font.size = Pt(12.5)
    p_a1.font.bold = True
    p_a1.font.color.rgb = COLOR_TEXT_MAIN

    p_a2 = tf_alg.add_paragraph()
    p_a2.text = "m1 (KMP, Rabin-Karp) | m2 (Suffix Array, Kasai's LCP) | m3 (Bitmask DP, Levenshtein) | m4 (Dinic Max Flow, Bipartite Matching) | m5 (3-SAT, Vertex Cover) | m6 (QuickSort, Reservoir Sampling)"
    p_a2.font.name = FONT_FAMILY
    p_a2.font.size = Pt(9.5)
    p_a2.font.color.rgb = COLOR_TEXT_MUTED
    p_a2.space_before = Pt(3)

    # Down Arrow 4
    arr4 = slide4.shapes.add_shape(MSO_SHAPE.DOWN_ARROW, Inches(6.46), Inches(5.82), Inches(0.4), Inches(0.18))
    arr4.fill.solid()
    arr4.fill.fore_color.rgb = COLOR_TEAL_PRIMARY
    arr4.line.fill.background()

    # Models & Data Service Layer (Layer 5)
    data_card = add_card(slide4, Inches(0.8), Inches(6.02), Inches(11.733), Inches(0.9), bg_color=COLOR_TEAL_BG, border_color=COLOR_TEAL_LIGHT)
    tf_dt = data_card.text_frame
    tf_dt.word_wrap = True
    tf_dt.margin_left = tf_dt.margin_right = Inches(0.2)
    tf_dt.margin_top = Inches(0.1)
    p_d1 = tf_dt.paragraphs[0]
    p_d1.text = "Data Domain Models & In-Memory Service Layer (src/model/ & src/service/)"
    p_d1.font.name = FONT_FAMILY
    p_d1.font.size = Pt(12.5)
    p_d1.font.bold = True
    p_d1.font.color.rgb = COLOR_DARK_NAVY

    p_d2 = tf_dt.add_paragraph()
    p_d2.text = "Domain Objects (Event.java, Participant.java, Activity.java, Venue.java, Volunteer.java) populated via in-memory DataService.java"
    p_d2.font.name = FONT_FAMILY
    p_d2.font.size = Pt(9.5)
    p_d2.font.color.rgb = COLOR_TEAL_PRIMARY
    p_d2.space_before = Pt(3)

    # =========================================================================
    # SLIDE 5: Application Interface
    # =========================================================================
    slide5 = prs.slides.add_slide(blank_layout)
    set_background(slide5, COLOR_BG_LIGHT)
    add_header(slide5, "Application Interface", "Genuine EventFlow System Interface Screen Captures")

    shots = [
        ("screenshots/dashboard.png", "System Overview Dashboard", "Displays high-level statistical summary cards (25 Total Events, 1250 Participants, 3420 Signups) and active event directory."),
        ("screenshots/events.png", "Event Management Directory", "Provides structured tabular view of all campus events with category dropdown filtering, status flags, and capacity tracking."),
        ("screenshots/m1_search.png", "Module M1 Pattern Search", "Demonstrates live execution of KMP and Rabin-Karp pattern matching algorithms on event title and description data.")
    ]

    shot_w = Inches(3.64)
    shot_h = Inches(4.3)
    shot_y = Inches(1.5)
    shot_sp = Inches(0.4)

    for i, (path, title, desc) in enumerate(shots):
        sx = Inches(0.8) + i * (shot_w + shot_sp)
        card = add_card(slide5, sx, shot_y, shot_w, Inches(5.35), accent_top=COLOR_TEAL_PRIMARY)

        if os.path.exists(path):
            slide5.shapes.add_picture(path, sx + Inches(0.12), shot_y + Inches(0.18), width=shot_w - Inches(0.24))

        tx_cap = slide5.shapes.add_textbox(sx + Inches(0.15), shot_y + Inches(2.75), shot_w - Inches(0.3), Inches(2.4))
        tf_cap = tx_cap.text_frame
        tf_cap.word_wrap = True
        tf_cap.margin_left = tf_cap.margin_right = tf_cap.margin_top = tf_cap.margin_bottom = 0

        p_ct = tf_cap.paragraphs[0]
        p_ct.text = title
        p_ct.font.name = FONT_FAMILY
        p_ct.font.size = Pt(14)
        p_ct.font.bold = True
        p_ct.font.color.rgb = COLOR_TEXT_MAIN

        p_cd = tf_cap.add_paragraph()
        p_cd.text = desc
        p_cd.font.name = FONT_FAMILY
        p_cd.font.size = Pt(11)
        p_cd.font.color.rgb = COLOR_TEXT_MUTED
        p_cd.space_before = Pt(6)

    # =========================================================================
    # SLIDE 6: DSA Modules (With Color Accents from UIUtils.java)
    # =========================================================================
    slide6 = prs.slides.add_slide(blank_layout)
    set_background(slide6, COLOR_BG_LIGHT)
    add_header(slide6, "DSA Modules", "Six Core Data Structures & Algorithmic Modules")

    dsa_modules = [
        (
            "Module M1", "String Pattern Matching",
            "Knuth-Morris-Pratt (KMP) & Rabin-Karp",
            "Executes exact pattern matching and rolling-hash searching across event titles and description records.",
            COLOR_M1_BLUE
        ),
        (
            "Module M2", "Document Similarity",
            "Suffix Array & Kasai's LCP Array",
            "Constructs suffix arrays and longest common prefixes to evaluate structural similarity in event documents.",
            COLOR_M2_CYAN
        ),
        (
            "Module M3", "Activity Optimization & Distance",
            "Bitmask Dynamic Programming & Levenshtein",
            "Computes optimal sub-event activity sequences and fuzzy string distances for typo-tolerant queries.",
            COLOR_M3_EMERALD
        ),
        (
            "Module M4", "Resource Allocation",
            "Dinic's Maximum Flow & Bipartite Matching",
            "Models capacity networks to allocate volunteers to events and optimize equipment distribution.",
            COLOR_M4_PURPLE
        ),
        (
            "Module M5", "Conflict Management",
            "3-SAT Solver & Vertex Cover Approximation",
            "Validates boolean scheduling constraints and computes 2-approximation vertex covers for venue monitoring.",
            COLOR_M5_AMBER
        ),
        (
            "Module M6", "Event Analytics",
            "Randomized QuickSort & Reservoir Sampling",
            "Ranks multi-attribute event records efficiently and selects uniform random samples for participant surveys.",
            COLOR_M6_ROSE
        )
    ]

    mod_w = Inches(3.64)
    mod_h = Inches(2.45)
    row1_y = Inches(1.5)
    row2_y = Inches(4.25)

    for i, (code, title, algos, desc, accent_clr) in enumerate(dsa_modules):
        r = i // 3
        c = i % 3
        mx = Inches(0.8) + c * (mod_w + Inches(0.4))
        my = row1_y if r == 0 else row2_y

        add_card(slide6, mx, my, mod_w, mod_h, accent_top=accent_clr)

        tx = slide6.shapes.add_textbox(mx + Inches(0.18), my + Inches(0.18), mod_w - Inches(0.36), mod_h - Inches(0.36))
        tf = tx.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0

        p_code = tf.paragraphs[0]
        p_code.text = code.upper() + "  •  " + title
        p_code.font.name = FONT_FAMILY
        p_code.font.size = Pt(11)
        p_code.font.bold = True
        p_code.font.color.rgb = accent_clr

        p_alg = tf.add_paragraph()
        p_alg.text = algos
        p_alg.font.name = FONT_FAMILY
        p_alg.font.size = Pt(13)
        p_alg.font.bold = True
        p_alg.font.color.rgb = COLOR_TEXT_MAIN
        p_alg.space_before = Pt(4)

        p_desc = tf.add_paragraph()
        p_desc.text = desc
        p_desc.font.name = FONT_FAMILY
        p_desc.font.size = Pt(10.5)
        p_desc.font.color.rgb = COLOR_TEXT_MUTED
        p_desc.space_before = Pt(6)

    # =========================================================================
    # SLIDE 7: Implementation and Technology
    # =========================================================================
    slide7 = prs.slides.add_slide(blank_layout)
    set_background(slide7, COLOR_BG_LIGHT)
    add_header(slide7, "Implementation and Technology", "Core Tech Stack & Algorithmic Integration Workflow")

    t1_x = Inches(0.8)
    t1_y = Inches(1.5)
    t_w = Inches(5.66)
    t_h = Inches(4.3)

    add_card(slide7, t1_x, t1_y, t_w, t_h, accent_top=COLOR_DARK_NAVY)

    tx_t1 = slide7.shapes.add_textbox(t1_x + Inches(0.25), t1_y + Inches(0.25), t_w - Inches(0.5), t_h - Inches(0.5))
    tf_t1 = tx_t1.text_frame
    tf_t1.word_wrap = True

    p_th1 = tf_t1.paragraphs[0]
    p_th1.text = "Technology Stack & Architecture"
    p_th1.font.name = FONT_FAMILY
    p_th1.font.size = Pt(18)
    p_th1.font.bold = True
    p_th1.font.color.rgb = COLOR_TEXT_MAIN

    tech_bullets = [
        ("Programming Language", "Java SE (JDK 21 tested, JDK 8+ compatible)."),
        ("UI Framework", "Pure Java Swing (JFrame, CardLayout, JTable, JPanel, Graphics2D) without external GUI libraries."),
        ("Design Paradigm", "Object-Oriented Programming (OOP) with clean encapsulation and model separation."),
        ("Modular Architecture", "Structured packages: main, ui, model, algorithms (m1-m6), service."),
        ("Data Management", "In-memory DataService providing pre-populated sample records for fast evaluation.")
    ]

    for title, desc in tech_bullets:
        p_bt = tf_t1.add_paragraph()
        p_bt.text = "• " + title + ": "
        p_bt.font.name = FONT_FAMILY
        p_bt.font.size = Pt(11.5)
        p_bt.font.bold = True
        p_bt.font.color.rgb = COLOR_TEXT_MAIN
        p_bt.space_before = Pt(8)

        run = p_bt.add_run()
        run.text = desc
        run.font.bold = False
        run.font.color.rgb = COLOR_TEXT_MUTED

    t2_x = Inches(6.87)
    add_card(slide7, t2_x, t1_y, t_w, t_h, accent_top=COLOR_TEAL_PRIMARY)

    tx_t2 = slide7.shapes.add_textbox(t2_x + Inches(0.25), t1_y + Inches(0.25), t_w - Inches(0.5), t_h - Inches(0.5))
    tf_t2 = tx_t2.text_frame
    tf_t2.word_wrap = True

    p_th2 = tf_t2.paragraphs[0]
    p_th2.text = "Component Integration Workflow"
    p_th2.font.name = FONT_FAMILY
    p_th2.font.size = Pt(18)
    p_th2.font.bold = True
    p_th2.font.color.rgb = COLOR_TEXT_MAIN

    flow_bullets = [
        ("User Interaction", "User triggers search, optimization, or allocation requests via Swing UI panels."),
        ("Service Coordination", "UI controllers invoke DataService to fetch active model collections."),
        ("In-Memory Processing", "Target DSA modules process objects in memory without disk I/O bottlenecks."),
        ("Result Wrapping", "Algorithms return structured outputs, match positions, or flow values."),
        ("Dynamic UI Rendering", "Swing components refresh custom JTable views and metric stat cards instantaneously.")
    ]

    for title, desc in flow_bullets:
        p_bt = tf_t2.add_paragraph()
        p_bt.text = "• " + title + ": "
        p_bt.font.name = FONT_FAMILY
        p_bt.font.size = Pt(11.5)
        p_bt.font.bold = True
        p_bt.font.color.rgb = COLOR_TEXT_MAIN
        p_bt.space_before = Pt(8)

        run = p_bt.add_run()
        run.text = desc
        run.font.bold = False
        run.font.color.rgb = COLOR_TEXT_MUTED

    fn_card = add_card(slide7, Inches(0.8), Inches(6.0), Inches(11.733), Inches(0.85), bg_color=COLOR_TEAL_BG, border_color=COLOR_TEAL_LIGHT)
    tx_fn = slide7.shapes.add_textbox(Inches(1.0), Inches(6.1), Inches(11.333), Inches(0.65))
    tf_fn = tx_fn.text_frame
    tf_fn.word_wrap = True
    p_fn = tf_fn.paragraphs[0]
    p_fn.text = "Note on Data Storage: Built as a pure Java desktop platform using in-memory data structures via DataService.java; does not require external database drivers or permanent database setup."
    p_fn.font.name = FONT_FAMILY
    p_fn.font.size = Pt(11.5)
    p_fn.font.bold = True
    p_fn.font.color.rgb = COLOR_DARK_NAVY

    # =========================================================================
    # SLIDE 8: Conclusion
    # =========================================================================
    slide8 = prs.slides.add_slide(blank_layout)
    set_background(slide8, COLOR_BG_LIGHT)
    add_header(slide8, "Conclusion", "Project Summary & Acknowledgements")

    sum_w = Inches(11.733)
    sum_h = Inches(3.2)
    sum_x = Inches(0.8)
    sum_y = Inches(1.5)

    add_card(slide8, sum_x, sum_y, sum_w, sum_h, accent_top=COLOR_TEAL_PRIMARY)

    tx_sum = slide8.shapes.add_textbox(sum_x + Inches(0.3), sum_y + Inches(0.25), sum_w - Inches(0.6), sum_h - Inches(0.5))
    tf_sum = tx_sum.text_frame
    tf_sum.word_wrap = True

    p_sh = tf_sum.paragraphs[0]
    p_sh.text = "Project Summary & Core Accomplishments"
    p_sh.font.name = FONT_FAMILY
    p_sh.font.size = Pt(18)
    p_sh.font.bold = True
    p_sh.font.color.rgb = COLOR_TEXT_MAIN

    concl_bullets = [
        "Centralized Event Administration: EventFlow successfully organizes college events, student registrations, and campus venues into a modern desktop platform.",
        "Practical Application of DSA: Implements 6 specialized DSA modules (KMP, Rabin-Karp, Suffix Array, Kasai's LCP, Bitmask DP, Levenshtein, Dinic Max-Flow, Bipartite Matching, 3-SAT, Vertex Cover, QuickSort, Reservoir Sampling) to solve real-world operational challenges.",
        "Clean Modular OOP Design: Strict decoupling of Swing presentation panels, domain models, in-memory data service, and algorithmic execution units."
    ]

    for b in concl_bullets:
        p_b = tf_sum.add_paragraph()
        p_b.text = "• " + b
        p_b.font.name = FONT_FAMILY
        p_b.font.size = Pt(12)
        p_b.font.color.rgb = COLOR_TEXT_MUTED
        p_b.space_before = Pt(10)

    ty_y = Inches(4.95)
    ty_h = Inches(1.9)
    ty_card = add_card(slide8, sum_x, ty_y, sum_w, ty_h, bg_color=COLOR_DARK_NAVY, border_color=None)

    ty_acc = slide8.shapes.add_shape(MSO_SHAPE.RECTANGLE, sum_x, ty_y, sum_w, Inches(0.08))
    ty_acc.fill.solid()
    ty_acc.fill.fore_color.rgb = COLOR_TEAL_LIGHT
    ty_acc.line.fill.background()

    tx_ty = slide8.shapes.add_textbox(sum_x + Inches(0.5), ty_y + Inches(0.3), sum_w - Inches(1.0), ty_h - Inches(0.6))
    tf_ty = tx_ty.text_frame
    tf_ty.word_wrap = True

    p_ty1 = tf_ty.paragraphs[0]
    p_ty1.text = "Thank You!"
    p_ty1.font.name = FONT_FAMILY
    p_ty1.font.size = Pt(32)
    p_ty1.font.bold = True
    p_ty1.font.color.rgb = COLOR_WHITE
    p_ty1.alignment = PP_ALIGN.CENTER

    p_ty2 = tf_ty.add_paragraph()
    p_ty2.text = "EventFlow — College Event Management Platform  |  Open for Questions & Discussion"
    p_ty2.font.name = FONT_FAMILY
    p_ty2.font.size = Pt(14)
    p_ty2.font.color.rgb = COLOR_TEAL_LIGHT
    p_ty2.alignment = PP_ALIGN.CENTER
    p_ty2.space_before = Pt(8)

    output_filename = "EventFlow_Presentation.pptx"
    prs.save(output_filename)
    print(f"Successfully regenerated PowerPoint presentation: {os.path.abspath(output_filename)}")

if __name__ == "__main__":
    create_presentation()
