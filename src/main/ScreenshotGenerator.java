package main;

import ui.MainFrame;

import javax.imageio.ImageIO;
import javax.swing.*;
import java.awt.*;
import java.awt.image.BufferedImage;
import java.io.File;
import java.lang.reflect.Field;
import java.lang.reflect.Method;

public class ScreenshotGenerator {
    public static void main(String[] args) throws Exception {
        System.setProperty("awt.useSystemAAFontSettings", "on");
        System.setProperty("swing.aatext", "true");
        UIManager.setLookAndFeel(UIManager.getSystemLookAndFeelClassName());

        SwingUtilities.invokeAndWait(() -> {
            try {
                MainFrame frame = new MainFrame();
                frame.setSize(1280, 800);
                frame.setLocationRelativeTo(null);
                frame.setVisible(true);

                File dir = new File("screenshots");
                if (!dir.exists()) dir.mkdirs();

                Field navButtonsField = MainFrame.class.getDeclaredField("navButtons");
                navButtonsField.setAccessible(true);
                JButton[] navButtons = (JButton[]) navButtonsField.get(frame);

                Method setActiveTabMethod = MainFrame.class.getDeclaredMethod("setActiveTab", JButton.class, String.class);
                setActiveTabMethod.setAccessible(true);

                String[] cardKeys = {
                        "DASHBOARD", "EVENTS", "PARTICIPANTS", "VENUES",
                        "M1", "M2", "M3", "M4", "M5", "M6"
                };

                String[] filenames = {
                        "dashboard.png", "events.png", "participants.png", "venues.png",
                        "m1_search.png", "m2_similarity.png", "m3_optimization.png",
                        "m4_resources.png", "m5_conflicts.png", "m6_analytics.png"
                };

                for (int i = 0; i < cardKeys.length; i++) {
                    setActiveTabMethod.invoke(frame, navButtons[i], cardKeys[i]);
                    frame.revalidate();
                    frame.repaint();
                    Thread.sleep(300);

                    BufferedImage image = new BufferedImage(1280, 800, BufferedImage.TYPE_INT_RGB);
                    Graphics2D g2d = image.createGraphics();
                    g2d.setRenderingHint(RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON);
                    g2d.setRenderingHint(RenderingHints.KEY_TEXT_ANTIALIASING, RenderingHints.VALUE_TEXT_ANTIALIAS_ON);
                    frame.paint(g2d);
                    g2d.dispose();

                    File outFile = new File(dir, filenames[i]);
                    ImageIO.write(image, "png", outFile);
                    System.out.println("Saved screenshot: " + outFile.getAbsolutePath());
                }

                frame.dispose();
            } catch (Exception e) {
                e.printStackTrace();
            }
        });

        System.exit(0);
    }
}
