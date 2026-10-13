package ui;

import algorithms.m5.ThreeSAT;
import algorithms.m5.ThreeSAT.Clause;
import algorithms.m5.ThreeSAT.SATResult;
import algorithms.m5.VertexCoverApproximation;
import algorithms.m5.VertexCoverApproximation.ConflictEdge;
import algorithms.m5.VertexCoverApproximation.VertexCoverResult;
import java.awt.*;
import java.util.List;
import javax.swing.*;
import javax.swing.border.EmptyBorder;
import javax.swing.table.DefaultTableModel;
import model.Activity;
import service.DataService;

/**
 * M5 - Scheduling Conflict Management UI Panel.
 * SECTION 1: Scheduling Constraint Satisfiability using 3-SAT (DPLL).
 * SECTION 2: Activity Conflict Resolution using Vertex Cover 2-Approximation.
 */
public class M5ConflictPanel extends JPanel {

    // Section 1: 3-SAT
    private JComboBox<String> cbSatPreset;
    private JTable tableSAT;
    private DefaultTableModel modelSAT;
    private JLabel lblSatStatus;
    private JLabel lblSatStats;
    private JLabel lblSatAssignment;

    // Section 2: Vertex Cover
    private final JTable tableVC;
    private final DefaultTableModel modelVC;
    private final JLabel lblVCStatus;
    private final JLabel lblVCStats;

    public M5ConflictPanel() {
        setLayout(new BorderLayout(15, 15));
        setBackground(UIUtils.COLOR_BG);
        setBorder(new EmptyBorder(20, 25, 20, 25));

        // Header & Banner
        JPanel topContainer = new JPanel(new BorderLayout(0, 10));
        topContainer.setOpaque(false);
        topContainer.add(UIUtils.createHeaderPanel(
                "Module M5: Scheduling Constraints & Conflict Resolution",
                "Uses 3-SAT DPLL to validate scheduling constraints and Vertex Cover 2-Approximation for activity conflict resolution."
        ), BorderLayout.NORTH);

        topContainer.add(UIUtils.createModuleBanner(
                "M5",
                "3-SAT DPLL & Vertex Cover 2-Approximation Engine",
                "SECTION 1: DPLL backtracking 3-SAT for schedule feasibility. SECTION 2: 2-Approximation Vertex Cover for conflict resolution.",
                "3-SAT (DPLL) / Vertex Cover 2-Approximation"
        ), BorderLayout.SOUTH);

        add(topContainer, BorderLayout.NORTH);

        JPanel centerPanel = new JPanel(new GridLayout(2, 1, 0, 15));
        centerPanel.setOpaque(false);

        // =========================================================================
        // SECTION 1: 3-SAT (DPLL Backtracking)
        // =========================================================================
        JPanel cardSAT = UIUtils.createCardPanel();
        cardSAT.setLayout(new BorderLayout(10, 10));
        cardSAT.setBorder(new EmptyBorder(12, 15, 12, 15));

        // Header
        JPanel satHeader = new JPanel(new BorderLayout());
        satHeader.setOpaque(false);

        JLabel lblSatTitle = new JLabel("SECTION 1: Scheduling Feasibility (3-SAT DPLL Solver)");
        lblSatTitle.setFont(UIUtils.FONT_SECTION);
        lblSatTitle.setForeground(UIUtils.COLOR_ROSE);

        JPanel satControls = new JPanel(new FlowLayout(FlowLayout.RIGHT, 10, 0));
        satControls.setOpaque(false);

        JLabel lblPreset = new JLabel("Constraint Scenario:");
        lblPreset.setFont(UIUtils.FONT_BOLD);

        cbSatPreset = new JComboBox<>(new String[]{
                "Scenario A: Hackathon Schedule (SAT)",
                "Scenario B: Complex Event Constraints (SAT)",
                "Scenario C: Forced Contradiction (UNSAT)",
                "Scenario D: Workshop Timing (SAT)"
        });
        cbSatPreset.setFont(UIUtils.FONT_REGULAR);
        cbSatPreset.addActionListener(e -> runSATSolver());

        JButton btnSolve = UIUtils.createStyledButton("Run 3-SAT Solver (DPLL)", UIUtils.COLOR_ROSE, Color.WHITE);
        btnSolve.addActionListener(e -> runSATSolver());

        satControls.add(lblPreset);
        satControls.add(cbSatPreset);
        satControls.add(btnSolve);

        satHeader.add(lblSatTitle, BorderLayout.WEST);
        satHeader.add(satControls, BorderLayout.EAST);

        cardSAT.add(satHeader, BorderLayout.NORTH);

        // 3-SAT Table
        String[] colsSAT = {"Clause #", "Literal 1", "Literal 2", "Literal 3", "Clause Form", "Clause Status"};
        modelSAT = new DefaultTableModel(colsSAT, 0) {
            @Override public boolean isCellEditable(int r, int c) { return false; }
        };

        tableSAT = new JTable(modelSAT);
        UIUtils.styleTable(tableSAT);

        JScrollPane spSAT = new JScrollPane(tableSAT);
        spSAT.setBorder(BorderFactory.createEmptyBorder());
        spSAT.getViewport().setBackground(Color.WHITE);

        cardSAT.add(spSAT, BorderLayout.CENTER);

        // 3-SAT Footer
        JPanel satFooter = new JPanel(new GridLayout(3, 1, 3, 3));
        satFooter.setOpaque(false);
        satFooter.setBorder(BorderFactory.createCompoundBorder(
                BorderFactory.createLineBorder(new Color(226, 232, 240), 1),
                new EmptyBorder(8, 10, 8, 10)
        ));
        satFooter.setBackground(new Color(248, 250, 252));

        lblSatStatus = new JLabel("Status: Select a scenario and run the 3-SAT DPLL Solver.");
        lblSatStatus.setFont(UIUtils.FONT_BOLD);
        lblSatStatus.setForeground(UIUtils.COLOR_TEXT_DARK);

        lblSatAssignment = new JLabel("Satisfying Assignment: N/A");
        lblSatAssignment.setFont(UIUtils.FONT_REGULAR);
        lblSatAssignment.setForeground(UIUtils.COLOR_TEXT_DARK);

        lblSatStats = new JLabel("Variables: 0 | Clauses: 0 | States Explored: 0 | Exec Time: 0 ns");
        lblSatStats.setFont(UIUtils.FONT_REGULAR);
        lblSatStats.setForeground(UIUtils.COLOR_TEXT_MUTED);

        satFooter.add(lblSatStatus);
        satFooter.add(lblSatAssignment);
        satFooter.add(lblSatStats);

        cardSAT.add(satFooter, BorderLayout.SOUTH);

        centerPanel.add(cardSAT);

        // =========================================================================
        // SECTION 2: Vertex Cover 2-Approximation
        // =========================================================================
        JPanel cardVC = UIUtils.createCardPanel();
        cardVC.setLayout(new BorderLayout(10, 10));
        cardVC.setBorder(new EmptyBorder(12, 15, 12, 15));

        JPanel vcHeader = new JPanel(new BorderLayout());
        vcHeader.setOpaque(false);

        JLabel lblVCTitle = new JLabel("SECTION 2: Activity Conflict Resolution (Vertex Cover 2-Approximation)");
        lblVCTitle.setFont(UIUtils.FONT_SECTION);
        lblVCTitle.setForeground(UIUtils.COLOR_PRIMARY);

        JButton btnVC = UIUtils.createStyledButton("Compute Vertex Cover (2-Approx)", UIUtils.COLOR_PRIMARY, Color.WHITE);
        btnVC.addActionListener(e -> runVertexCover());

        vcHeader.add(lblVCTitle, BorderLayout.WEST);
        vcHeader.add(btnVC, BorderLayout.EAST);

        cardVC.add(vcHeader, BorderLayout.NORTH);

        // VC Table
        String[] colsVC = {"Activity ID", "Activity Title", "Conflict With", "Conflict Reason", "Duration (mins)", "Cover Status"};
        modelVC = new DefaultTableModel(colsVC, 0) {
            @Override public boolean isCellEditable(int r, int c) { return false; }
        };

        tableVC = new JTable(modelVC);
        UIUtils.styleTable(tableVC);

        JScrollPane spVC = new JScrollPane(tableVC);
        spVC.setBorder(BorderFactory.createEmptyBorder());
        spVC.getViewport().setBackground(Color.WHITE);

        cardVC.add(spVC, BorderLayout.CENTER);

        // VC Footer
        JPanel vcFooter = new JPanel(new GridLayout(2, 1, 3, 3));
        vcFooter.setOpaque(false);
        vcFooter.setBorder(BorderFactory.createCompoundBorder(
                BorderFactory.createLineBorder(new Color(226, 232, 240), 1),
                new EmptyBorder(8, 10, 8, 10)
        ));
        vcFooter.setBackground(new Color(248, 250, 252));

        lblVCStatus = new JLabel("Status: Ready to run Vertex Cover 2-Approximation on activity conflict graph.");
        lblVCStatus.setFont(UIUtils.FONT_BOLD);
        lblVCStatus.setForeground(UIUtils.COLOR_PRIMARY);

        lblVCStats = new JLabel("Cover Size: 0 | Total Conflicts: 0 | All Edges Covered: N/A | Exec Time: 0 ns");
        lblVCStats.setFont(UIUtils.FONT_REGULAR);
        lblVCStats.setForeground(UIUtils.COLOR_TEXT_MUTED);

        vcFooter.add(lblVCStatus);
        vcFooter.add(lblVCStats);

        cardVC.add(vcFooter, BorderLayout.SOUTH);

        centerPanel.add(cardVC);

        add(centerPanel, BorderLayout.CENTER);

        // Initial runs on panel load
        runSATSolver();
        runVertexCover();
    }

    // -------------------------------------------------------------------------
    // SECTION 1: 3-SAT Solver
    // -------------------------------------------------------------------------
    private void runSATSolver() {
        int scenario = cbSatPreset.getSelectedIndex();

        ThreeSAT sat;
        String scenarioDesc;

        switch (scenario) {
            case 0:
                // Scenario A: Hackathon scheduling (SAT)
                // Variables: x1=Keynote, x2=CodingPhase, x3=ProjectDemo, x4=TeamRegistration, x5=JudgesPanel
                sat = new ThreeSAT(5);
                scenarioDesc = "Hackathon Schedule - 5 time-slots, 5 clauses";
                sat.addClause(1, false, 2, false, 3, true);   // x1 OR x2 OR NOT x3
                sat.addClause(1, true,  2, false, 4, false);  // NOT x1 OR x2 OR x4
                sat.addClause(3, false, 4, true,  5, false);  // x3 OR NOT x4 OR x5
                sat.addClause(1, false, 3, false, 5, true);   // x1 OR x3 OR NOT x5
                sat.addClause(2, true,  4, false, 5, false);  // NOT x2 OR x4 OR x5
                break;
            case 1:
                // Scenario B: Complex multi-event constraints (SAT)
                sat = new ThreeSAT(6);
                scenarioDesc = "Complex Multi-Event Constraints - 6 variables, 6 clauses";
                sat.addClause(1, false, 2, true,  3, false);
                sat.addClause(2, false, 4, false, 5, true);
                sat.addClause(3, true,  4, false, 6, false);
                sat.addClause(1, true,  5, false, 6, true);
                sat.addClause(2, false, 3, true,  6, false);
                sat.addClause(1, false, 4, true,  5, false);
                break;
            case 2:
                // Scenario C: Forced contradiction (UNSAT)
                // x1 must be TRUE (clause 1), x1 must be FALSE (clause 4),
                // and no way to satisfy both
                sat = new ThreeSAT(3);
                scenarioDesc = "Forced Contradiction - 3 variables, 8 contradictory clauses (UNSAT)";
                // All 8 combinations of (x1,x2,x3) are forbidden
                sat.addClause(1, false, 2, false, 3, false);
                sat.addClause(1, false, 2, false, 3, true);
                sat.addClause(1, false, 2, true,  3, false);
                sat.addClause(1, false, 2, true,  3, true);
                sat.addClause(1, true,  2, false, 3, false);
                sat.addClause(1, true,  2, false, 3, true);
                sat.addClause(1, true,  2, true,  3, false);
                sat.addClause(1, true,  2, true,  3, true);
                break;
            default:
                // Scenario D: Workshop timing (SAT)
                sat = new ThreeSAT(4);
                scenarioDesc = "Workshop Timing Constraints - 4 variables, 4 clauses";
                sat.addClause(1, false, 2, true,  3, false);  // Room A or not Room B or Room C
                sat.addClause(2, false, 3, true,  4, false);  // Room B or not Room C or Room D
                sat.addClause(1, true,  3, false, 4, false);  // not Room A or Room C or Room D
                sat.addClause(1, false, 2, false, 4, true);   // Room A or Room B or not Room D
                break;
        }

        modelSAT.setRowCount(0);
        List<Clause> clauses = sat.getClauses();

        long startTime = System.nanoTime();
        SATResult result = sat.solve();
        long elapsedNs = System.nanoTime() - startTime;
        double elapsedMs = elapsedNs / 1_000_000.0;

        // Populate clause table
        for (int i = 0; i < clauses.size(); i++) {
            Clause c = clauses.get(i);
            String clauseStatus = result.satisfiable ? (c.isSatisfied(result.assignment) ? "SATISFIED ✓" : "UNSATISFIED") : "UNSAT (No Assignment)";
            String lit1 = c.literals[0].toString();
            String lit2 = c.literals[1].toString();
            String lit3 = c.literals[2].toString();
            modelSAT.addRow(new Object[]{
                    "C" + (i + 1),
                    lit1,
                    lit2,
                    lit3,
                    c.toString(),
                    clauseStatus
            });
        }

        if (result.satisfiable) {
            lblSatStatus.setForeground(new Color(16, 185, 129)); // Emerald
            lblSatStatus.setText("SATISFIABLE (SAT): The scheduling constraints are feasible. Satisfying assignment found.");

            StringBuilder sb = new StringBuilder("Assignment: ");
            for (int v = 1; v <= result.numVariables; v++) {
                if (v > 1) sb.append(" | ");
                sb.append("x").append(v).append("=").append(result.assignment[v] == 1 ? "TRUE" : "FALSE");
            }
            lblSatAssignment.setText(sb.toString());
        } else {
            lblSatStatus.setForeground(new Color(225, 29, 72)); // Rose
            lblSatStatus.setText("UNSATISFIABLE (UNSAT): No valid scheduling assignment exists. Constraints are contradictory.");
            lblSatAssignment.setText("Satisfying Assignment: None — all " + result.statesExplored + " states exhausted.");
        }

        lblSatStats.setText(String.format("Scenario: %s | Variables: %d | Clauses: %d | States Explored: %d | Exec Time: %,d ns (%.3f ms)",
                scenarioDesc, result.numVariables, result.numClauses, result.statesExplored, elapsedNs, elapsedMs));
    }

    // -------------------------------------------------------------------------
    // SECTION 2: Vertex Cover 2-Approximation
    // -------------------------------------------------------------------------
    private void runVertexCover() {
        List<Activity> activities = DataService.getInstance().getActivities();
        int n = activities.size();

        if (n < 2) {
            lblVCStatus.setForeground(new Color(225, 29, 72));
            lblVCStatus.setText("No conflict graph: Need at least 2 activities to form conflict edges.");
            return;
        }

        VertexCoverApproximation vc = new VertexCoverApproximation(n);

        // Build conflict edges: two activities conflict when they share the same room
        // or when their durations overlap within the same event (same eventId, overlapping windows)
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                Activity a = activities.get(i);
                Activity b = activities.get(j);

                boolean sameRoom = a.getRoom().equalsIgnoreCase(b.getRoom());
                boolean sameEvent = a.getEventId().equalsIgnoreCase(b.getEventId());

                if (sameRoom) {
                    vc.addConflictEdge(i, j, "Same Room: " + a.getRoom());
                } else if (sameEvent) {
                    vc.addConflictEdge(i, j, "Same Event Overlap (" + a.getEventId() + ")");
                }
            }
        }

        long startTime = System.nanoTime();
        VertexCoverResult result = vc.computeVertexCover();
        long elapsedNs = System.nanoTime() - startTime;
        double elapsedMs = elapsedNs / 1_000_000.0;

        modelVC.setRowCount(0);

        for (int i = 0; i < n; i++) {
            Activity act = activities.get(i);
            boolean inCover = result.coverSet.contains(i);

            // Find any conflicts this activity has
            String conflictsWith = "None";
            String conflictReason = "-";
            for (ConflictEdge e : result.allEdges) {
                if (e.u == i || e.v == i) {
                    int other = (e.u == i) ? e.v : e.u;
                    conflictsWith = activities.get(other).getId();
                    conflictReason = e.description;
                    break;
                }
            }

            modelVC.addRow(new Object[]{
                    act.getId(),
                    act.getTitle(),
                    conflictsWith,
                    conflictReason,
                    act.getDurationMinutes() + " mins",
                    inCover ? "IN COVER (Conflict Resolved)" : "NOT IN COVER (No Conflict)"
            });
        }

        boolean coverValid = result.isCoverValid();

        lblVCStatus.setForeground(new Color(16, 185, 129)); // Emerald
        lblVCStatus.setText(String.format(
                "Vertex Cover 2-Approx Complete: %d activity/activities selected in cover | All edges covered: %s",
                result.coverSize, coverValid ? "YES ✓" : "NO ✗"));

        lblVCStats.setText(String.format(
                "Cover Size: %d | Total Conflict Edges: %d | Cover Valid (all edges covered): %s | Exec Time: %,d ns (%.3f ms)",
                result.coverSize, result.totalEdges, coverValid ? "YES" : "NO", elapsedNs, elapsedMs));
    }
}
