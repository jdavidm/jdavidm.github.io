import re
import random

with open('publications.html', 'r') as f:
    html = f.read()

# I will recreate the injected Working Papers and Book Chapters to *exactly* mimic the HTML of a journal article card:
# Example:
# <div class="pub-card has-bg-image" data-category="article" style="background: linear-gradient(to bottom, rgba(15, 23, 42, 0.4) 0%, rgba(15, 23, 42, 0.7) 100%), url('...'); background-size: cover; background-position: center;">
#     <span class="card-tag" style="background-color: var(--color-primary-light); color: white;">Journal Article</span>
#     <h3 class="pub-title">...</h3>
#     <p class="pub-authors">...</p>
#     <p class="pub-journal">...</p>
#     <div class="pub-links">...</div>
# </div>

images = ['photos/IMG_8410-2.jpg', 'photos/DSC_0216.jpg', 'photos/IMG_9513.jpg', 'photos/IMG_7551.jpg', 'photos/IMG_2588.JPG']
img_idx = 0

def get_image():
    global img_idx
    img = images[img_idx % len(images)]
    img_idx += 1
    return img

working_papers = [
    {
        "title": "The Uses (and Misuses) of Weather and Earth Observation Data in Geospatial Impact Evaluations",
        "authors": "Benami, E., M. Cecil, A. Josephson, G. Maskell, and J.D. Michler",
        "link": "http://arxiv.org/abs/2510.05108",
        "link_text": "View Paper"
    },
    {
        "title": "Considerations and Resources for Integrating EO and Socioeconomic Data",
        "authors": "Michler, J.D., E. Benami, A. Josephson, G. Maskell, M. Cecil, P. Behrer, R. Heilmayr, S. Gourlay, and K.Singh"
    },
    {
        "title": "Mining Meaning: Conducting AI-Assisted Reviews of Economic Literature",
        "authors": "Michler, J.D., K. Douglas, and A. Josephson"
    },
    {
        "title": "Variable Selection in Socioeconomic Applications of Remotely Sensed Weather Data: Insights from the LSMS-ISA",
        "authors": "Michler, J.D., A. Josephson, C.D. Agme and T. Kilic"
    },
    {
        "title": "Labor, Credit, and Markets: Evidence from the Philippines, 1971-2016",
        "authors": "Kee-Tui, E., A. Josephson, and J.D. Michler"
    },
    {
        "title": "Risk and Rainfall: Specification Sensitivity in Estimating Smallholder Risk Preferences",
        "authors": "Braham, R., A. Josephson, and J.D. Michler"
    },
    {
        "title": "Approximation in Complex Pricing Mechanisms",
        "authors": "Michler, J.D., P. Slade, and S.Y. Wu"
    },
    {
        "title": "Complex Pricing and Consumer Behavior: Evidence from a Lab Experiment",
        "authors": "Deutschmann, J.W., J.D. Michler, and E. Tjernström"
    },
    {
        "title": "A Dynamic Model of Firm Location in Two-Dimensional Space",
        "authors": "Michler, J.D., S.D. Yun, and B. Gramig"
    },
    {
        "title": "An Industrious Revolution? Changes in the Household Economy in Rural Bangladesh",
        "authors": "Josephson, A., J.D. Michler, and A. Orr"
    },
    {
        "title": "Effects of Credit and Market Access on Farm Gate Prices in India",
        "authors": "Baylis, K., M. Mallory, J.D. Michler, and T. Songsermsawa"
    }
]

working_papers_html = '    <!-- Working Papers Section -->\n    <h2 class="section-title" style="margin-top: 3rem;">Working Papers</h2>\n    <div class="pub-grid animate-on-scroll">\n'
for wp in working_papers:
    link_html = f'<div class="pub-links">\n                    <a href="{wp["link"]}" target="_blank" rel="noopener noreferrer"<i class="fas fa-external-link-alt"></i> {wp["link_text"]}</a>\n                </div>' if "link" in wp else ''

    working_papers_html += f"""
        <div class="pub-card has-bg-image" data-category="working" style="background: linear-gradient(to bottom, rgba(15, 23, 42, 0.4) 0%, rgba(15, 23, 42, 0.7) 100%), url('{get_image()}'); background-size: cover; background-position: center;">
            <span class="card-tag" style="background-color: var(--color-secondary); color: white;">Working Paper</span>
            <h3 class="pub-title">{wp['title']}</h3>
            <p class="pub-authors">{wp['authors']}</p>
            {link_html}
        </div>
"""
working_papers_html += '    </div>\n'

book_chapters = [
    {
        "title": "Recent Developments in Inference: Practicalities for the Applied Economist",
        "authors": "Michler, J.D. and A. Josephson. 2022.",
        "journal": "In J. Roosen and J.E. Hobbs, eds., A Modern Guide to Food Economics. Cheltenham: Edward Elgar Publishing.",
        "link": "https://doi.org/10.4337/9781800372054.00019",
        "link_text": "View Chapter"
    },
    {
        "title": "The Evolving Impact of COVID-19 in Four African Countries",
        "authors": "Furbush, A., A. Josephson, T. Kilic, and J.D. Michler. 2021.",
        "journal": "In R. Arezki, S. Djankov, and U. Panizza, eds., Shaping Africa’s Post-Covid Recovery. London: CEPR Press.",
        "link": "https://voxeu.org/content/shaping-africa-s-post-covid-recovery",
        "link_text": "View Chapter",
        "extra_link": "https://documents.worldbank.org/en/publication/documents-reports/documentdetail/810651614623398314/the-evolving-socioeconomic-impacts-of-covid-19-in-four-african-countries",
        "extra_text": "Working Paper"
    }
]

book_chapters_html = '    <!-- Book Chapters Section -->\n    <h2 class="section-title" style="margin-top: 3rem;">Book Chapters</h2>\n    <div class="pub-grid animate-on-scroll">\n'
for bc in book_chapters:
    extra = f'\n                    <a href="{bc["extra_link"]}" target="_blank" rel="noopener noreferrer"<i class="fas fa-file-pdf"></i> {bc["extra_text"]}</a>' if "extra_link" in bc else ''

    book_chapters_html += f"""
        <div class="pub-card has-bg-image" data-category="book" style="background: linear-gradient(to bottom, rgba(15, 23, 42, 0.4) 0%, rgba(15, 23, 42, 0.7) 100%), url('{get_image()}'); background-size: cover; background-position: center;">
            <span class="card-tag" style="background-color: var(--color-accent); color: white;">Book Chapter</span>
            <h3 class="pub-title">{bc['title']}</h3>
            <p class="pub-authors">{bc['authors']}</p>
            <p class="pub-journal">{bc['journal']}</p>
            <div class="pub-links">
                <a href="{bc['link']}" target="_blank" rel="noopener noreferrer"<i class="fas fa-external-link-alt"></i> {bc['link_text']}</a>{extra}
            </div>
        </div>
"""
book_chapters_html += '    </div>\n'

# Remove the old injected sections
html = re.sub(r'<!-- Book Chapters Section -->.*?</main>', '</main>', html, flags=re.DOTALL)
html = html.replace('</main>', book_chapters_html + "\n" + working_papers_html + "\n    </main>")

with open('publications.html', 'w') as f:
    f.write(html)
