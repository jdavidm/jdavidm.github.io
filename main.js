document.addEventListener("DOMContentLoaded", () => {
  // Intersection Observer for scroll animations
  const observerOptions = {
    root: null,
    rootMargin: "0px",
    threshold: 0.1,
  };

  const observer = new IntersectionObserver((entries, observer) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add("is-visible");
        observer.unobserve(entry.target); // Only animate once
      }
    });
  }, observerOptions);

  // Select elements to animate
  const animateElements = document.querySelectorAll(".animate-on-scroll");
  animateElements.forEach((el) => observer.observe(el));

  // Update active state in navigation based on scroll position (for single page sections if any)
  // and highlight current page based on pathname
  const currentPath = window.location.pathname.split("/").pop() || "index.html";
  const navLinks = document.querySelectorAll(".nav-link");

  navLinks.forEach((link) => {
    const linkPath = link.getAttribute("href");
    if (
      linkPath === currentPath ||
      (currentPath === "" && linkPath === "index.html")
    ) {
      link.classList.add("active");
    } else {
      // For sections on the same page (e.g. #about)
      if (linkPath.startsWith("#") && currentPath === "index.html") {
        // Simple scroll spy logic could go here if needed
      }
    }
  });

  // Mobile Navigation Toggle
  const mobileBtn = document.createElement("button");
  mobileBtn.classList.add("mobile-menu-btn");
  mobileBtn.innerHTML = '<i class="fas fa-bars"></i>';
  mobileBtn.style.display = "none"; // Controlled by CSS
  mobileBtn.style.background = "none";
  mobileBtn.style.border = "none";
  mobileBtn.style.fontSize = "1.5rem";
  mobileBtn.style.color = "var(--color-primary)";
  mobileBtn.style.cursor = "pointer";

  const navContainer = document.querySelector(".nav-container");
  const navUl = document.querySelector(".nav-links");

  if (navContainer && navUl) {
    navContainer.appendChild(mobileBtn);

    // Simple CSS injection for mobile menu logic
    const style = document.createElement("style");
    style.textContent = `
            @media (max-width: 768px) {
                .mobile-menu-btn { display: block !important; }
                .nav-links {
                    position: absolute;
                    top: 100%;
                    left: 0;
                    width: 100%;
                    background: white;
                    flex-direction: column;
                    padding: 1rem;
                    gap: 1rem;
                    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
                    display: none;
                }
                .nav-links.show { display: flex; }
            }
        `;
    document.head.appendChild(style);

    mobileBtn.addEventListener("click", () => {
      navUl.classList.toggle("show");
      const icon = mobileBtn.querySelector("i");
      if (navUl.classList.contains("show")) {
        icon.classList.remove("fa-bars");
        icon.classList.add("fa-times");
      } else {
        icon.classList.remove("fa-times");
        icon.classList.add("fa-bars");
      }
    });
  }
});
