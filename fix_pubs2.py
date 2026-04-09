import re

with open('publications.html', 'r') as f:
    html = f.read()

# Working papers to insert
working_papers_html = """
    <!-- Working Papers Section -->
    <h2 class="section-title" style="margin-top: 3rem;">Working Papers</h2>
    <div class="pub-grid">
        <div class="pub-card" data-category="working" style="background-image: linear-gradient(rgba(0, 0, 0, 0.4), rgba(0, 0, 0, 0.7)), url('photos/IMG_8410-2.jpg'); color: white;">
            <div class="card-overlay" style="padding: 1.5rem; position: relative; z-index: 2;">
                <h3 class="pub-title" style="color: white; font-weight: 600; margin-bottom: 0.5rem;">The Uses (and Misuses) of Weather and Earth Observation Data in Geospatial Impact Evaluations</h3>
                <p class="pub-authors" style="color: #e2e8f0; font-size: 0.95rem; margin-bottom: 0.5rem;">Benami, E., M. Cecil, A. Josephson, G. Maskell, and J.D. Michler</p>
                <div class="pub-links" style="margin-top: 1rem;">
                    <a href="http://arxiv.org/abs/2510.05108" target="_blank" rel="noopener noreferrer"<i class="fas fa-external-link-alt"></i> View Paper</a>
                </div>
            </div>
        </div>

        <div class="pub-card" data-category="working" style="background-image: linear-gradient(rgba(0, 0, 0, 0.4), rgba(0, 0, 0, 0.7)), url('photos/DSC_0216.jpg'); color: white;">
            <div class="card-overlay" style="padding: 1.5rem; position: relative; z-index: 2;">
                <h3 class="pub-title" style="color: white; font-weight: 600; margin-bottom: 0.5rem;">Considerations and Resources for Integrating EO and Socioeconomic Data</h3>
                <p class="pub-authors" style="color: #e2e8f0; font-size: 0.95rem; margin-bottom: 0.5rem;">Michler, J.D., E. Benami, A. Josephson, G. Maskell, M. Cecil, P. Behrer, R. Heilmayr, S. Gourlay, and K.Singh</p>
            </div>
        </div>

        <div class="pub-card" data-category="working" style="background-image: linear-gradient(rgba(0, 0, 0, 0.4), rgba(0, 0, 0, 0.7)), url('photos/IMG_9513.jpg'); color: white;">
            <div class="card-overlay" style="padding: 1.5rem; position: relative; z-index: 2;">
                <h3 class="pub-title" style="color: white; font-weight: 600; margin-bottom: 0.5rem;">Mining Meaning: Conducting AI-Assisted Reviews of Economic Literature</h3>
                <p class="pub-authors" style="color: #e2e8f0; font-size: 0.95rem; margin-bottom: 0.5rem;">Michler, J.D., K. Douglas, and A. Josephson</p>
            </div>
        </div>

        <div class="pub-card" data-category="working" style="background-image: linear-gradient(rgba(0, 0, 0, 0.4), rgba(0, 0, 0, 0.7)), url('photos/IMG_7551.jpg'); color: white;">
            <div class="card-overlay" style="padding: 1.5rem; position: relative; z-index: 2;">
                <h3 class="pub-title" style="color: white; font-weight: 600; margin-bottom: 0.5rem;">Variable Selection in Socioeconomic Applications of Remotely Sensed Weather Data: Insights from the LSMS-ISA</h3>
                <p class="pub-authors" style="color: #e2e8f0; font-size: 0.95rem; margin-bottom: 0.5rem;">Michler, J.D., A. Josephson, C.D. Agme and T. Kilic</p>
            </div>
        </div>

        <div class="pub-card" data-category="working" style="background-image: linear-gradient(rgba(0, 0, 0, 0.4), rgba(0, 0, 0, 0.7)), url('photos/IMG_2588.JPG'); color: white;">
            <div class="card-overlay" style="padding: 1.5rem; position: relative; z-index: 2;">
                <h3 class="pub-title" style="color: white; font-weight: 600; margin-bottom: 0.5rem;">Labor, Credit, and Markets: Evidence from the Philippines, 1971-2016</h3>
                <p class="pub-authors" style="color: #e2e8f0; font-size: 0.95rem; margin-bottom: 0.5rem;">Kee-Tui, E., A. Josephson, and J.D. Michler</p>
            </div>
        </div>

        <div class="pub-card" data-category="working" style="background-image: linear-gradient(rgba(0, 0, 0, 0.4), rgba(0, 0, 0, 0.7)), url('photos/DSC_0216.jpg'); color: white;">
            <div class="card-overlay" style="padding: 1.5rem; position: relative; z-index: 2;">
                <h3 class="pub-title" style="color: white; font-weight: 600; margin-bottom: 0.5rem;">Risk and Rainfall: Specification Sensitivity in Estimating Smallholder Risk Preferences</h3>
                <p class="pub-authors" style="color: #e2e8f0; font-size: 0.95rem; margin-bottom: 0.5rem;">Braham, R., A. Josephson, and J.D. Michler</p>
            </div>
        </div>

        <div class="pub-card" data-category="working" style="background-image: linear-gradient(rgba(0, 0, 0, 0.4), rgba(0, 0, 0, 0.7)), url('photos/IMG_8410-2.jpg'); color: white;">
            <div class="card-overlay" style="padding: 1.5rem; position: relative; z-index: 2;">
                <h3 class="pub-title" style="color: white; font-weight: 600; margin-bottom: 0.5rem;">Approximation in Complex Pricing Mechanisms</h3>
                <p class="pub-authors" style="color: #e2e8f0; font-size: 0.95rem; margin-bottom: 0.5rem;">Michler, J.D., P. Slade, and S.Y. Wu</p>
            </div>
        </div>

        <div class="pub-card" data-category="working" style="background-image: linear-gradient(rgba(0, 0, 0, 0.4), rgba(0, 0, 0, 0.7)), url('photos/IMG_9513.jpg'); color: white;">
            <div class="card-overlay" style="padding: 1.5rem; position: relative; z-index: 2;">
                <h3 class="pub-title" style="color: white; font-weight: 600; margin-bottom: 0.5rem;">Complex Pricing and Consumer Behavior: Evidence from a Lab Experiment</h3>
                <p class="pub-authors" style="color: #e2e8f0; font-size: 0.95rem; margin-bottom: 0.5rem;">Deutschmann, J.W., J.D. Michler, and E. Tjernström</p>
            </div>
        </div>

        <div class="pub-card" data-category="working" style="background-image: linear-gradient(rgba(0, 0, 0, 0.4), rgba(0, 0, 0, 0.7)), url('photos/IMG_7551.jpg'); color: white;">
            <div class="card-overlay" style="padding: 1.5rem; position: relative; z-index: 2;">
                <h3 class="pub-title" style="color: white; font-weight: 600; margin-bottom: 0.5rem;">A Dynamic Model of Firm Location in Two-Dimensional Space</h3>
                <p class="pub-authors" style="color: #e2e8f0; font-size: 0.95rem; margin-bottom: 0.5rem;">Michler, J.D., S.D. Yun, and B. Gramig</p>
            </div>
        </div>

        <div class="pub-card" data-category="working" style="background-image: linear-gradient(rgba(0, 0, 0, 0.4), rgba(0, 0, 0, 0.7)), url('photos/IMG_2588.JPG'); color: white;">
            <div class="card-overlay" style="padding: 1.5rem; position: relative; z-index: 2;">
                <h3 class="pub-title" style="color: white; font-weight: 600; margin-bottom: 0.5rem;">An Industrious Revolution? Changes in the Household Economy in Rural Bangladesh</h3>
                <p class="pub-authors" style="color: #e2e8f0; font-size: 0.95rem; margin-bottom: 0.5rem;">Josephson, A., J.D. Michler, and A. Orr</p>
            </div>
        </div>

        <div class="pub-card" data-category="working" style="background-image: linear-gradient(rgba(0, 0, 0, 0.4), rgba(0, 0, 0, 0.7)), url('photos/IMG_8410-2.jpg'); color: white;">
            <div class="card-overlay" style="padding: 1.5rem; position: relative; z-index: 2;">
                <h3 class="pub-title" style="color: white; font-weight: 600; margin-bottom: 0.5rem;">Effects of Credit and Market Access on Farm Gate Prices in India</h3>
                <p class="pub-authors" style="color: #e2e8f0; font-size: 0.95rem; margin-bottom: 0.5rem;">Baylis, K., M. Mallory, J.D. Michler, and T. Songsermsawa</p>
            </div>
        </div>
    </div>
"""

# Book chapters to insert
book_chapters_html = """
    <!-- Book Chapters Section -->
    <h2 class="section-title" style="margin-top: 3rem;">Book Chapters</h2>
    <div class="pub-grid">
        <div class="pub-card" data-category="book" style="background-image: linear-gradient(rgba(0, 0, 0, 0.4), rgba(0, 0, 0, 0.7)), url('photos/DSC_0216.jpg'); color: white;">
            <div class="card-overlay" style="padding: 1.5rem; position: relative; z-index: 2;">
                <h3 class="pub-title" style="color: white; font-weight: 600; margin-bottom: 0.5rem;">Recent Developments in Inference: Practicalities for the Applied Economist</h3>
                <p class="pub-authors" style="color: #e2e8f0; font-size: 0.95rem; margin-bottom: 0.5rem;">Michler, J.D. and A. Josephson. 2022.</p>
                <p class="pub-journal" style="color: #cbd5e1; font-style: italic; font-size: 0.9rem;">In J. Roosen and J.E. Hobbs, eds., A Modern Guide to Food Economics. Cheltenham: Edward Elgar Publishing.</p>
                <div class="pub-links" style="margin-top: 1rem;">
                    <a href="https://doi.org/10.4337/9781800372054.00019" target="_blank" rel="noopener noreferrer"<i class="fas fa-external-link-alt"></i> View Chapter</a>
                </div>
            </div>
        </div>

        <div class="pub-card" data-category="book" style="background-image: linear-gradient(rgba(0, 0, 0, 0.4), rgba(0, 0, 0, 0.7)), url('photos/IMG_9513.jpg'); color: white;">
            <div class="card-overlay" style="padding: 1.5rem; position: relative; z-index: 2;">
                <h3 class="pub-title" style="color: white; font-weight: 600; margin-bottom: 0.5rem;">The Evolving Impact of COVID-19 in Four African Countries</h3>
                <p class="pub-authors" style="color: #e2e8f0; font-size: 0.95rem; margin-bottom: 0.5rem;">Furbush, A., A. Josephson, T. Kilic, and J.D. Michler. 2021.</p>
                <p class="pub-journal" style="color: #cbd5e1; font-style: italic; font-size: 0.9rem;">In R. Arezki, S. Djankov, and U. Panizza, eds., Shaping Africa’s Post-Covid Recovery. London: CEPR Press.</p>
                <div class="pub-links" style="margin-top: 1rem;">
                    <a href="https://voxeu.org/content/shaping-africa-s-post-covid-recovery" target="_blank" rel="noopener noreferrer"<i class="fas fa-external-link-alt"></i> View Chapter</a>
                    <a href="https://documents.worldbank.org/en/publication/documents-reports/documentdetail/810651614623398314/the-evolving-socioeconomic-impacts-of-covid-19-in-four-african-countries" target="_blank" rel="noopener noreferrer"<i class="fas fa-file-pdf"></i> Working Paper</a>
                </div>
            </div>
        </div>
    </div>
"""

# Find where to insert them - right after the Journal Articles grid ends
if "</div>\n    </main>" in html:
    html = html.replace("</div>\n    </main>", "</div>\n" + book_chapters_html + "\n" + working_papers_html + "\n    </main>")
elif "        </div>\n      </div>\n    </main>" in html: # Based on the earlier grep output
    html = html.replace("        </div>\n      </div>\n    </main>", "        </div>\n" + book_chapters_html + "\n" + working_papers_html + "\n      </div>\n    </main>")


with open('publications.html', 'w') as f:
    f.write(html)
