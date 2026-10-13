# EventFlow - College DSA Event Management Platform

EventFlow is a modern Java Swing desktop application designed for large-scale college event management. It features a clean modular architecture and provides interactive user interface panels for managing events, participants, venues, and specialized Data Structures & Algorithms (DSA) processing modules.

---

## 📁 Project Structure

```
EventFlow/
├── src/
│   ├── main/
│   │   └── Main.java                    # Entry point of the application
│   ├── model/
│   │   ├── Event.java                   # Event data model
│   │   ├── Participant.java             # Participant model
│   │   ├── Activity.java                # Sub-event / Activity model
│   │   ├── Venue.java                   # Venue facility model
│   │   └── Volunteer.java               # Volunteer model
│   ├── ui/
│   │   ├── MainFrame.java               # Main window JFrame with dark sidebar navigation
│   │   ├── DashboardPanel.java          # High-level statistics overview & active events
│   │   ├── EventPanel.java              # Event directory JTable & filter controls
│   │   ├── ParticipantPanel.java        # Student registrations JTable & search
│   │   ├── VenuePanel.java              # Campus auditoriums & lab seating JTable
│   │   ├── M1SearchPanel.java           # Module 1 UI (KMP / Rabin-Karp Search)
│   │   ├── M2DocumentPanel.java         # Module 2 UI (Suffix Array / LCP)
│   │   ├── M3OptimizationPanel.java     # Module 3 UI (Bitmask DP / Levenshtein Distance)
│   │   ├── M4ResourcePanel.java         # Module 4 UI (Dinic Max Flow / Bipartite Matching)
│   │   ├── M5ConflictPanel.java         # Module 5 UI (3-SAT / Vertex Cover Approximation)
│   │   ├── M6AnalyticsPanel.java        # Module 6 UI (Randomized QuickSort / Reservoir Sampling)
│   │   └── UIUtils.java                 # Theme styling, fonts, stat cards & JTable formatting
│   ├── algorithms/
│   │   ├── m1/                          # Structure for String Pattern Matching (KMP, Rabin-Karp)
│   │   ├── m2/                          # Suffix Array and LCP using Kasai's Algorithm
│   │   ├── m3/                          # Bitmask Dynamic Programming and Levenshtein Distance
│   │   ├── m4/                          # Dinic Maximum Flow and Bipartite Matching
│   │   ├── m5/                          # 3-SAT and Vertex Cover 2-Approximation
│   │   └── m6/                          # Randomized QuickSort and Reservoir Sampling
│   └── service/
│       └── DataService.java             # In-memory sample data provider
└── README.md
```

---

## 🚀 How to Run the Application

### Prerequisites
- **Java SE Development Kit (JDK) 8 or higher** (JDK 21 tested & supported).

### Step 1: Navigate to the `EventFlow` directory
Open PowerShell or your command prompt in the project root:
```bash
cd EventFlow
```

### Step 2: Compile Java Source Files
Create a build output directory `bin` and compile all `.java` files:

#### On Windows (PowerShell):
```powershell
mkdir bin -Force
javac -d bin (Get-ChildItem -Recurse -Filter *.java src).FullName
```

#### On Linux / macOS / Bash:
```bash
mkdir -p bin
javac -d bin $(find src -name "*.java")
```

### Step 3: Run the Application
Execute `Main` from the compiled `bin` folder:

```bash
java -cp bin main.Main
```

---

## 📊 Summary of Implemented Requirements

1. **Pure Java Swing GUI**: Built entirely with standard Swing components (`JFrame`, `CardLayout`, `JTable`, `JPanel`, `JButton`, `JLabel`) without external UI libraries or JavaFX.
2. **Modular Architecture**: Model-View-Service separation keeping UI panels decoupled and `Main.java` lightweight.
3. **CardLayout Navigation**: Responsive left sidebar with instant tab switching across 10 views.
4. **Dashboard Metrics**:
   - Total Events: **25**
   - Participants: **1250**
   - Registrations: **3420**
   - Active Events: **8**
5. **Sample Data**: 25 pre-populated sample event records, student participants, campus venues, activities, and volunteers.
6. **Implemented DSA Algorithms**: The six modules provide the following algorithms:
   - **M1 / CO1**: KMP; Rabin-Karp
   - **M2 / CO2**: Suffix Array; LCP using Kasai's Algorithm
   - **M3 / CO3**: Bitmask Dynamic Programming; Levenshtein Distance
   - **M4 / CO4**: Dinic Maximum Flow; Bipartite Matching
   - **M5 / CO5**: 3-SAT; Vertex Cover 2-Approximation
   - **M6 / CO6**: Randomized QuickSort; Reservoir Sampling
