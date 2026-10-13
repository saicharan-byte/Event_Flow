package service;

import model.Event;
import model.Participant;
import model.Venue;
import model.Activity;
import model.Volunteer;

import java.util.ArrayList;
import java.util.List;

/**
 * Service providing in-memory sample data for the EventFlow application.
 */
public class DataService {
    private static DataService instance;

    private final List<Event> events;
    private final List<Participant> participants;
    private final List<Venue> venues;
    private final List<Activity> activities;
    private final List<Volunteer> volunteers;

    private DataService() {
        events = new ArrayList<>();
        participants = new ArrayList<>();
        venues = new ArrayList<>();
        activities = new ArrayList<>();
        volunteers = new ArrayList<>();

        initSampleData();
    }

    public static synchronized DataService getInstance() {
        if (instance == null) {
            instance = new DataService();
        }
        return instance;
    }

    private void initSampleData() {
        // 25 Sample Events (8 Active, 12 Upcoming, 5 Completed)
        events.add(new Event("EVT-101", "Hackathon 2026 - CodeFest", "Technology", "2026-10-01", "09:00 AM", "Main Auditorium", 300, 280, "Active", "Annual 24-hour coding challenge and TechFest hackathon for developers."));
        events.add(new Event("EVT-102", "AI & Deep Learning Workshop", "Academic", "2026-10-02", "10:00 AM", "Lab 302", 80, 78, "Active", "Hands-on workshop on neural networks, computer vision, and TechFest AI projects."));
        events.add(new Event("EVT-103", "Annual Cultural Fest - Rhythm 26", "Cultural", "2026-10-03", "05:00 PM", "Open Air Theatre", 1500, 1420, "Active", "Mega annual festival showcasing music, dance, and creative performing arts."));
        events.add(new Event("EVT-104", "Inter-College Robotics League", "Technology", "2026-10-04", "11:00 AM", "Indoor Sports Complex", 400, 310, "Active", "Robotics design competition and autonomous bot battles at TechFest arena."));
        events.add(new Event("EVT-105", "Cyber Security Symposium", "Technology", "2026-10-05", "09:30 AM", "Seminar Hall A", 200, 190, "Active", "Ethical hacking, threat analysis, and network defense technical symposium."));
        events.add(new Event("EVT-106", "Design Thinking & UI/UX Summit", "Workshop", "2026-10-06", "02:00 PM", "Design Studio", 60, 58, "Active", "Interactive workshop on user experience, prototyping, and design systems."));
        events.add(new Event("EVT-107", "Annual Athletics Championship", "Sports", "2026-10-07", "08:00 AM", "University Ground", 800, 750, "Active", "Track and field events including sprint, relay, long jump, and shot put."));
        events.add(new Event("EVT-108", "Startup & Innovation Expo", "Academic", "2026-10-08", "10:30 AM", "Innovation Hub", 250, 240, "Active", "Showcase of student startup ideas, tech prototypes, and venture pitches."));

        events.add(new Event("EVT-109", "Cloud Architecture Masterclass", "Technology", "2026-10-12", "10:00 AM", "Lab 302", 100, 85, "Upcoming", "Masterclass on microservices, AWS cloud infrastructure, and DevOps pipelines."));
        events.add(new Event("EVT-110", "Battle of the Bands", "Cultural", "2026-10-15", "06:00 PM", "Open Air Theatre", 1000, 620, "Upcoming", "Live music contest featuring rock, pop, and indie college bands."));
        events.add(new Event("EVT-111", "Inter-Department Basketball", "Sports", "2026-10-18", "03:00 PM", "Indoor Sports Complex", 300, 180, "Upcoming", "Knockout basketball tournament between university departments."));
        events.add(new Event("EVT-112", "Quantum Computing Seminar", "Academic", "2026-10-20", "11:00 AM", "Seminar Hall B", 150, 95, "Upcoming", "Guest lecture on quantum algorithms, qubits, and future computing paradigms."));
        events.add(new Event("EVT-113", "Data Science Career Fair", "Academic", "2026-10-22", "09:00 AM", "Main Auditorium", 600, 410, "Upcoming", "Networking event connecting analytics students with industry recruiters."));
        events.add(new Event("EVT-114", "Photography & Short Film Fest", "Cultural", "2026-10-25", "01:00 PM", "Media Lab", 120, 90, "Upcoming", "Exhibition of creative photography and screening of original short films."));
        events.add(new Event("EVT-115", "Web Development Bootcamp", "Workshop", "2026-10-28", "10:00 AM", "Lab 105", 70, 65, "Upcoming", "Full-stack web creation bootcamp covering HTML, CSS, JavaScript, and React."));
        events.add(new Event("EVT-116", "E-Sports Championship (Valorant)", "Gaming", "2026-11-01", "12:00 PM", "E-Sports Arena", 250, 230, "Upcoming", "Multi-player tactical shooter tournament for university gaming enthusiasts."));
        events.add(new Event("EVT-117", "Model United Nations (MUN)", "Academic", "2026-11-04", "09:00 AM", "Conference Hall A", 180, 140, "Upcoming", "Diplomatic simulation debate on international security and global policy."));
        events.add(new Event("EVT-118", "Chess & Strategy Tournament", "Sports", "2026-11-08", "10:00 AM", "Student Center", 60, 50, "Upcoming", "Rapid chess competition testing strategic thinking and tactical play."));
        events.add(new Event("EVT-119", "Environmental Sustainability Talk", "Academic", "2026-11-12", "02:30 PM", "Seminar Hall A", 200, 110, "Upcoming", "Seminar on renewable energy, carbon footprint reduction, and green tech."));
        events.add(new Event("EVT-120", "Drama Club Annual Play", "Cultural", "2026-11-15", "06:30 PM", "Main Auditorium", 500, 320, "Upcoming", "Theatrical production presented by the campus drama society."));

        events.add(new Event("EVT-121", "Freshers Welcome Party 2026", "Cultural", "2026-09-01", "05:00 PM", "Open Air Theatre", 1200, 1200, "Completed", "Welcome ceremony and evening celebration for incoming first-year students."));
        events.add(new Event("EVT-122", "Alumni Networking Dinner", "Academic", "2026-09-10", "07:00 PM", "Banquet Hall", 200, 195, "Completed", "Annual alumni gathering for mentorship and professional networking."));
        events.add(new Event("EVT-123", "Orientation & Campus Tour", "Academic", "2026-09-15", "09:00 AM", "Main Auditorium", 800, 780, "Completed", "Guided campus tour and academic orientation program for new batches."));
        events.add(new Event("EVT-124", "Inter-College Debate Cup", "Academic", "2026-09-20", "11:00 AM", "Seminar Hall A", 150, 145, "Completed", "Parliamentary style debate cup on technology ethics and society."));
        events.add(new Event("EVT-125", "Code Debugging Contest", "Technology", "2026-09-25", "02:00 PM", "Lab 302", 90, 88, "Completed", "Timed competition to identify and fix algorithmic bugs in complex code."));

        // Sample Venues
        venues.add(new Venue("V-101", "Main Auditorium", "Central Block, Ground Floor", 1500, "Projector, Sound System, Stage, Air Conditioned", true));
        venues.add(new Venue("V-102", "Open Air Theatre", "Campus South Lawn", 2000, "Lighting, Sound System, Open Seating", true));
        venues.add(new Venue("V-103", "Indoor Sports Complex", "Sports Wing, Block C", 800, "Basketball Court, Badminton Courts, Bleachers", false));
        venues.add(new Venue("V-104", "Seminar Hall A", "Academic Block 1, Floor 2", 200, "Podium, Projector, Mic System, WiFi", true));
        venues.add(new Venue("V-105", "Lab 302 (Computer Center)", "IT Building, Floor 3", 100, "80 Workstations, LAN, Smart Board", true));
        venues.add(new Venue("V-106", "Innovation Hub", "R&D Complex, Floor 1", 250, "Modular Desks, Display Screens, 3D Printers", true));
        venues.add(new Venue("V-107", "Design Studio", "Arts & Architecture Wing", 60, "Drafting Tables, High-End Workstations", false));

        // Sample Participants
        participants.add(new Participant("P-1001", "Alice Vance", "alice.v@univ.edu", "Computer Science", "Hackathon 2026 - CodeFest", "2026-09-28", "Confirmed"));
        participants.add(new Participant("P-1002", "Bob Martinez", "bob.m@univ.edu", "Electrical Engg", "Hackathon 2026 - CodeFest", "2026-09-28", "Confirmed"));
        participants.add(new Participant("P-1003", "Charlie Davis", "charlie.d@univ.edu", "Mechanical Engg", "Annual Cultural Fest", "2026-09-29", "Confirmed"));
        participants.add(new Participant("P-1004", "Diana Prince", "diana.p@univ.edu", "Information Tech", "AI & Deep Learning Workshop", "2026-09-29", "Confirmed"));
        participants.add(new Participant("P-1005", "Ethan Hunt", "ethan.h@univ.edu", "Cyber Security", "Cyber Security Symposium", "2026-09-30", "Waitlisted"));
        participants.add(new Participant("P-1006", "Fiona Gallagher", "fiona.g@univ.edu", "Business Studies", "Startup & Innovation Expo", "2026-09-30", "Confirmed"));
        participants.add(new Participant("P-1007", "George Clark", "george.c@univ.edu", "Civil Engg", "Annual Athletics Championship", "2026-09-30", "Confirmed"));
        participants.add(new Participant("P-1008", "Hannah Abbott", "hannah.a@univ.edu", "Biotechnology", "AI & Deep Learning Workshop", "2026-10-01", "Confirmed"));
        participants.add(new Participant("P-1009", "Ian Wright", "ian.w@univ.edu", "Computer Science", "Cloud Architecture Masterclass", "2026-10-01", "Waitlisted"));
        participants.add(new Participant("P-1010", "Julia Roberts", "julia.r@univ.edu", "Media & Arts", "Design Thinking & UI/UX", "2026-10-01", "Confirmed"));

        // Sample Activities (with Duration in Minutes and Priority Value)
        activities.add(new Activity("ACT-1", "EVT-101", "Keynote: Future of AI in Software", "09:30 AM", "10:30 AM", "Dr. Alan Turing", "Main Hall", 60, 95));
        activities.add(new Activity("ACT-2", "EVT-101", "Coding Phase 1: Problem Solving", "10:45 AM", "01:00 PM", "Mentors Team", "Auditorium Lab", 135, 85));
        activities.add(new Activity("ACT-3", "EVT-101", "Final Project Demos & Jury Evaluation", "02:00 PM", "04:30 PM", "Industry Judges", "Main Stage", 150, 90));
        activities.add(new Activity("ACT-4", "EVT-102", "Deep Learning Hands-On Lab", "10:00 AM", "11:30 AM", "Prof. Andrew Ng", "Lab 302", 90, 80));
        activities.add(new Activity("ACT-5", "EVT-102", "Neural Network Architecture Workshop", "11:45 AM", "01:15 PM", "Dr. Yann LeCun", "Lab 302", 90, 88));
        activities.add(new Activity("ACT-6", "EVT-103", "Cultural Music & Band Performance", "05:00 PM", "06:30 PM", "Campus Band", "Open Air Theatre", 90, 75));
        activities.add(new Activity("ACT-7", "EVT-105", "Ethical Hacking Live Demo", "09:30 AM", "10:15 AM", "Security Team", "Seminar Hall A", 45, 70));
        activities.add(new Activity("ACT-8", "EVT-106", "UI/UX Interactive Design Sprint", "02:00 PM", "03:00 PM", "Lead Designer", "Design Studio", 60, 65));

        // Sample Volunteers
        volunteers.add(new Volunteer("VOL-1", "Sarah Jenkins", "Registration Lead", "EVT-101", "+1 555-0143"));
        volunteers.add(new Volunteer("VOL-2", "Marcus Brody", "Technical Setup Coordinator", "EVT-101", "+1 555-0188"));
        volunteers.add(new Volunteer("VOL-3", "Elena Rostova", "Stage Manager", "EVT-103", "+1 555-0192"));
        volunteers.add(new Volunteer("VOL-4", "David Miller", "Hospitality & Logistics", "EVT-104", "+1 555-0176"));
        volunteers.add(new Volunteer("VOL-5", "Rachel Green", "Lab Technical Assistant", "EVT-102", "+1 555-0199"));
        volunteers.add(new Volunteer("VOL-6", "Alex Mercer", "Cyber Security Helper", "EVT-105", "+1 555-0211"));
        volunteers.add(new Volunteer("VOL-7", "Jessica Alba", "Design Studio Mentor", "EVT-106", "+1 555-0233"));
        volunteers.add(new Volunteer("VOL-8", "Chris Evans", "General Event Coordinator", "EVT-102", "+1 555-0255"));
    }

    public List<Event> getEvents() { return events; }
    public List<Participant> getParticipants() { return participants; }
    public List<Venue> getVenues() { return venues; }
    public List<Activity> getActivities() { return activities; }
    public List<Volunteer> getVolunteers() { return volunteers; }

    // Dashboard Statistics required by specifications:
    // Total Events: 25
    // Participants: 1250
    // Registrations: 3420
    // Active Events: 8
    public int getTotalEventsCount() { return 25; }
    public int getParticipantsCount() { return 1250; }
    public int getRegistrationsCount() { return 3420; }
    public int getActiveEventsCount() { return 8; }
}
