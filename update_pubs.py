import re

with open('publications.html', 'r') as f:
    html = f.read()

# Working papers to insert
working_papers_html = """
    <!-- Working Papers Section -->
    <h2 class="section-title">Working Papers</h2>
    <div class="publication-grid">
        <div class="publication-card" style="background-image: url('photos/IMG_8410-2.jpg');">
            <div class="card-overlay">
                <h3>The Uses (and Misuses) of Weather and Earth Observation Data in Geospatial Impact Evaluations</h3>
                <p>Benami, E., M. Cecil, A. Josephson, G. Maskell, and J.D. Michler</p>
                <div class="pub-links">
                    <a href="http://arxiv.org/abs/2510.05108" target="_blank" rel="noopener noreferrer">View Paper</a>
                </div>
            </div>
        </div>

        <div class="publication-card" style="background-image: url('photos/DSC_0216.jpg');">
            <div class="card-overlay">
                <h3>Considerations and Resources for Integrating EO and Socioeconomic Data</h3>
                <p>Michler, J.D., E. Benami, A. Josephson, G. Maskell, M. Cecil, P. Behrer, R. Heilmayr, S. Gourlay, and K.Singh</p>
            </div>
        </div>

        <div class="publication-card" style="background-image: url('photos/IMG_9513.jpg');">
            <div class="card-overlay">
                <h3>Mining Meaning: Conducting AI-Assisted Reviews of Economic Literature</h3>
                <p>Michler, J.D., K. Douglas, and A. Josephson</p>
            </div>
        </div>

        <div class="publication-card" style="background-image: url('photos/IMG_7551.jpg');">
            <div class="card-overlay">
                <h3>Variable Selection in Socioeconomic Applications of Remotely Sensed Weather Data: Insights from the LSMS-ISA</h3>
                <p>Michler, J.D., A. Josephson, C.D. Agme and T. Kilic</p>
            </div>
        </div>

        <div class="publication-card" style="background-image: url('photos/IMG_2588.JPG');">
            <div class="card-overlay">
                <h3>Labor, Credit, and Markets: Evidence from the Philippines, 1971-2016</h3>
                <p>Kee-Tui, E., A. Josephson, and J.D. Michler</p>
            </div>
        </div>

        <div class="publication-card" style="background-image: url('photos/DSC_0216.jpg');">
            <div class="card-overlay">
                <h3>Risk and Rainfall: Specification Sensitivity in Estimating Smallholder Risk Preferences</h3>
                <p>Braham, R., A. Josephson, and J.D. Michler</p>
            </div>
        </div>

        <div class="publication-card" style="background-image: url('photos/IMG_8410-2.jpg');">
            <div class="card-overlay">
                <h3>Approximation in Complex Pricing Mechanisms</h3>
                <p>Michler, J.D., P. Slade, and S.Y. Wu</p>
            </div>
        </div>

        <div class="publication-card" style="background-image: url('photos/IMG_9513.jpg');">
            <div class="card-overlay">
                <h3>Complex Pricing and Consumer Behavior: Evidence from a Lab Experiment</h3>
                <p>Deutschmann, J.W., J.D. Michler, and E. Tjernström</p>
            </div>
        </div>

        <div class="publication-card" style="background-image: url('photos/IMG_7551.jpg');">
            <div class="card-overlay">
                <h3>A Dynamic Model of Firm Location in Two-Dimensional Space</h3>
                <p>Michler, J.D., S.D. Yun, and B. Gramig</p>
            </div>
        </div>

        <div class="publication-card" style="background-image: url('photos/IMG_2588.JPG');">
            <div class="card-overlay">
                <h3>An Industrious Revolution? Changes in the Household Economy in Rural Bangladesh</h3>
                <p>Josephson, A., J.D. Michler, and A. Orr</p>
            </div>
        </div>

        <div class="publication-card" style="background-image: url('photos/IMG_8410-2.jpg');">
            <div class="card-overlay">
                <h3>Effects of Credit and Market Access on Farm Gate Prices in India</h3>
                <p>Baylis, K., M. Mallory, J.D. Michler, and T. Songsermsawa</p>
            </div>
        </div>
    </div>
"""

# Book chapters to insert
book_chapters_html = """
    <!-- Book Chapters Section -->
    <h2 class="section-title">Book Chapters</h2>
    <div class="publication-grid">
        <div class="publication-card" style="background-image: url('photos/DSC_0216.jpg');">
            <div class="card-overlay">
                <h3>Recent Developments in Inference: Practicalities for the Applied Economist</h3>
                <p>Michler, J.D. and A. Josephson. 2022.</p>
                <p class="journal-name">In J. Roosen and J.E. Hobbs, eds., A Modern Guide to Food Economics. Cheltenham: Edward Elgar Publishing.</p>
                <div class="pub-links">
                    <a href="https://doi.org/10.4337/9781800372054.00019" target="_blank" rel="noopener noreferrer">View Chapter</a>
                </div>
            </div>
        </div>

        <div class="publication-card" style="background-image: url('photos/IMG_9513.jpg');">
            <div class="card-overlay">
                <h3>The Evolving Impact of COVID-19 in Four African Countries</h3>
                <p>Furbush, A., A. Josephson, T. Kilic, and J.D. Michler. 2021.</p>
                <p class="journal-name">In R. Arezki, S. Djankov, and U. Panizza, eds., Shaping Africa’s Post-Covid Recovery. London: CEPR Press.</p>
                <div class="pub-links">
                    <a href="https://voxeu.org/content/shaping-africa-s-post-covid-recovery" target="_blank" rel="noopener noreferrer">View Chapter</a>
                    <a href="https://documents.worldbank.org/en/publication/documents-reports/documentdetail/810651614623398314/the-evolving-socioeconomic-impacts-of-covid-19-in-four-african-countries" target="_blank" rel="noopener noreferrer">Working Paper</a>
                </div>
            </div>
        </div>
    </div>
"""

# Find where to insert them - right after the Journal Articles grid ends
closing_grid_tag = "    </div>\n\n    </main>"

if "</div>\n    </main>" in html:
    html = html.replace("</div>\n    </main>", "</div>\n" + working_papers_html + "\n" + book_chapters_html + "\n    </main>")
elif "    </div>\n\n    <!-- Footer -->" in html:
    html = html.replace("    </div>\n\n    <!-- Footer -->", "    </div>\n\n" + working_papers_html + "\n" + book_chapters_html + "\n    <!-- Footer -->")
else:
    # Just a fallback find
    match = re.search(r'(</div>\s*</main>)', html)
    if match:
        html = html[:match.start()] + "</div>\n" + working_papers_html + "\n" + book_chapters_html + "\n" + match.group(1) + html[match.end():]


with open('publications.html', 'w') as f:
    f.write(html)
