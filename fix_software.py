with open('software.html', 'w') as f:
    f.write('''<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Software | Jeffrey D. Michler</title>
    <meta name="description" content="Software and econometric packages by Jeffrey D. Michler." />
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link
      href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Merriweather:ital,wght@0,300;0,400;1,300&display=swap"
      rel="stylesheet"
    />
    <!-- FontAwesome for Icons -->
    <link
      rel="stylesheet"
      href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css"
    />
    <!-- Core CSS -->
    <link rel="stylesheet" href="style.css" />
  </head>
  <body>
    <!-- Navigation Bar -->
    <nav class="navbar">
      <div class="nav-container container">
        <a href="index.html" class="nav-logo">Jeffrey D. Michler</a>
        <div class="hamburger">
          <span class="bar"></span>
          <span class="bar"></span>
          <span class="bar"></span>
        </div>
        <ul class="nav-links">
          <li><a href="index.html" class="nav-link">Home</a></li>
          <li><a href="cv.html" class="nav-link">CV & Bio</a></li>
          <li><a href="publications.html" class="nav-link">Publications</a></li>
          <li><a href="teaching.html" class="nav-link">Teaching</a></li>
          <li><a href="software.html" class="nav-link active">Software</a></li>
          <li>
            <a
              href="https://aidelab.arizona.edu/"
              class="nav-link"
              target="_blank" rel="noopener noreferrer"
              >AIDE Lab <i class="fas fa-external-link-alt" style="font-size: 0.8em"></i></a
            >
          </li>
        </ul>
      </div>
    </nav>

    <!-- Page Header (Hero Section) -->
    <header class="hero" style="min-height: 40vh">
      <img
        src="photos/IMG_2588.JPG"
        alt="Software Hero Background"
        class="hero-bg"
      />
      <div class="container relative z-10">
        <div class="hero-content text-center">
          <h1>Software</h1>
          <p class="subtitle">Econometric packages and tools</p>
        </div>
      </div>
    </header>

    <!-- Main Content Area -->
    <main class="section">
      <div class="container">

        <div style="display: grid; gap: var(--spacing-lg);">
            <!-- randcoef -->
            <div class="card" style="padding: var(--spacing-lg); background-color: var(--color-bg-surface); border-radius: var(--radius-lg); box-shadow: var(--shadow-sm); border: 1px solid var(--color-border);">
              <h2 style="color: var(--color-primary); margin-bottom: 1rem; border-bottom: 2px solid var(--color-accent); display: inline-block; padding-bottom: 0.5rem;">randcoef</h2>
              <p style="font-size: 1.1rem; color: var(--color-text-muted); margin-bottom: 1rem;">
                <strong>Description:</strong> Correlated Random Effects Estimation of the Random Coefficients Model
              </p>
              <p style="line-height: 1.7; margin-bottom: 1.5rem;">
                <code>randcoef</code> is a Stata module that estimates the
                Correlated Random Effects (CRE) model for panel data. It provides an
                alternative to traditional fixed effects or random effects by
                allowing for correlation between the unobserved heterogeneity and
                the observed regressors.
              </p>
              <a
                href="https://ideas.repec.org/c/boc/bocode/s458514.html"
                target="_blank" rel="noopener noreferrer"
                class="btn btn-primary"
              >
                <i class="fas fa-external-link-alt"></i> View on IDEAS/RePEc
              </a>
            </div>

            <!-- wxsum -->
            <div class="card" style="padding: var(--spacing-lg); background-color: var(--color-bg-surface); border-radius: var(--radius-lg); box-shadow: var(--shadow-sm); border: 1px solid var(--color-border);">
              <h2 style="color: var(--color-primary); margin-bottom: 1rem; border-bottom: 2px solid var(--color-accent); display: inline-block; padding-bottom: 0.5rem;">wxsum</h2>
              <p style="font-size: 1.1rem; color: var(--color-text-muted); margin-bottom: 1rem;">
                <strong>Description:</strong> Summary Statistics with Spatial Weights
              </p>
              <p style="line-height: 1.7; margin-bottom: 1.5rem;">
                <code>wxsum</code> is a Stata module to calculate summary statistics
                that incorporate spatial weighting matrices. This is particularly
                useful in spatial econometrics to understand the distribution of
                variables across geographical space or networks.
              </p>
              <a
                href="https://ideas.repec.org/c/boc/bocode/s458428.html"
                target="_blank" rel="noopener noreferrer"
                class="btn btn-primary"
              >
                <i class="fas fa-external-link-alt"></i> View on IDEAS/RePEc
              </a>
            </div>
        </div>

      </div>
    </main>

    <!-- Footer -->
    <footer class="footer">
      <div class="container footer-content">
        <div>
          <p>
            &copy;
            <script>
              document.write(new Date().getFullYear());
            </script>
            Jeffrey D. Michler. All rights reserved.
          </p>
          <p style="color: var(--color-text-muted); font-size: 0.9rem">
            McClelland Park 301K | Tucson, AZ 85721 |
            <a
              href="mailto:jdmichler@arizona.edu"
              style="color: var(--color-text-muted); text-decoration: underline"
              >jdmichler@arizona.edu</a
            >
          </p>
        </div>
        <div class="social-links">
          <a href="mailto:jdmichler@arizona.edu" title="Email"
            ><i class="fas fa-envelope"></i
          ></a>
          <a
            href="https://aaec.arizona.edu/person/jeffrey-d-michler"
            title="Departmental Website"
            target="_blank" rel="noopener noreferrer"
            ><i class="fas fa-university"></i
          ></a>
          <a
            href="https://orcid.org/0000-0001-7778-8703"
            title="ORCiD"
            target="_blank" rel="noopener noreferrer"
            ><i class="fab fa-orcid"></i
          ></a>
          <a
            href="https://scholar.google.com/citations?user=akcW2fkAAAAJ"
            title="Google Scholar"
            target="_blank" rel="noopener noreferrer"
            ><i class="fas fa-graduation-cap"></i
          ></a>
          <a href="https://github.com/jdavidm" title="GitHub" target="_blank" rel="noopener noreferrer"
            ><i class="fab fa-github"></i
          ></a>
        </div>
      </div>
    </footer>

    <!-- Core JS -->
    <script src="main.js"></script>
  </body>
</html>''')
