/**
 * AARANYA UNIVERSITY — INTERACTIVE CAMPUS MAP ENGINE
 * Script: map.js
 * Comprehensive 21-Landmark Directory & Visual SVG Interactive Engine
 */

const CAMPUS_LANDMARKS = [
  {
    id: 1,
    name: "Main Entrance & Welcome Center",
    category: "admin",
    tagline: "The Ceremonial Gateway to Aaranya",
    description: "Welcoming scholars, visitors, and dignitaries. Home to the Visitor Center, Security Operations, and the Admissions Welcome Desk.",
    highlights: ["Visitor Registration Desk", "Admissions Information Lounge", "City Transit Shuttle Bay"],
    coords: { x: 385, y: 110 }
  },
  {
    id: 2,
    name: "Administrative Block",
    category: "admin",
    tagline: "University Governance & Leadership",
    description: "Houses the Office of the Chancellor, Vice-Chancellor, Academic Senate Chamber, Registrar, and Financial Administration.",
    highlights: ["Chancellor's Boardroom", "Office of Academic Affairs", "Registrar & Student Records"],
    coords: { x: 525, y: 155 }
  },
  {
    id: 3,
    name: "School of Computer Sciences",
    category: "academic",
    tagline: "Code · Create · Collaborate · Change",
    description: "Cutting-edge computational research clusters, AI development suites, robotics testbeds, and collaborative software engineering studios.",
    highlights: ["AI & Data Science Labs", "HCI & Systems Labs", "Hackathon Arena", "High-Performance Computing Cluster"],
    coords: { x: 435, y: 255 }
  },
  {
    id: 4,
    name: "School of Liberal Arts & Sciences",
    category: "academic",
    tagline: "People · Perspectives · Possibilities",
    description: "Four core divisions: Humanities, Social Sciences, Natural Sciences, and Interdisciplinary Studies. Features Socratic seminar tables and anthropology displays.",
    highlights: ["Socratic Seminar Suites", "Natural Sciences Wet Labs", "Cognitive Science Observatory", "Philosophy Reading Room"],
    coords: { x: 615, y: 255 }
  },
  {
    id: 5,
    name: "School of Law",
    category: "academic",
    tagline: "Ideas · Justice · Society · Change",
    description: "Dedicated to legal scholarship and systemic justice. Contains an international moot court complex, legal aid clinics, and constitutional law chambers.",
    highlights: ["Moot Court Complex", "Free Legal Aid Clinic", "Human Rights Research Cell", "Constitutional Law Library"],
    coords: { x: 715, y: 345 }
  },
  {
    id: 6,
    name: "School of Business & Economics",
    category: "academic",
    tagline: "Insight · Innovation · Impact",
    description: "Combining analytical rigor with human insight. Features Bloomberg finance terminals, case-study amphitheaters, and executive management suites.",
    highlights: ["Bloomberg Trading Terminal Suite", "Social Enterprise Incubator", "Executive Case Theaters", "Behavioral Economics Lab"],
    coords: { x: 415, y: 400 }
  },
  {
    id: 7,
    name: "Central Library (The Nexus)",
    category: "academic",
    tagline: "Knowledge for a Kinder World",
    description: "A sweeping architectural masterpiece overlooking Aaranya Lake. Houses over 250,000 volumes, 24/7 silent study pods, and digital research terminals.",
    highlights: ["Panoramic Lake View Reading Pods", "24/7 Graduate Research Floor", "Rare Manuscripts & Archives", "Digital Scholarly Repository"],
    coords: { x: 605, y: 435 }
  },
  {
    id: 8,
    name: "Research & Innovation Hub",
    category: "research",
    tagline: "Ideas into Impact",
    description: "Venture incubation center, rapid prototyping makerspace, clean-tech testbeds, and technology transfer offices for student and faculty startups.",
    highlights: ["Rapid Prototyping & 3D Print Lab", "Clean Energy Sandbox", "Venture Seed Accelerator", "Patent & Licensing Desk"],
    coords: { x: 685, y: 460 }
  },
  {
    id: 9,
    name: "Auditorium & Convention Center",
    category: "culture",
    tagline: "The Grand Stage for Thought & Art",
    description: "A 1,500-seat state-of-the-art acoustic auditorium hosting national symposia, international academic conferences, dramatic arts, and convocations.",
    highlights: ["1,500-Seat Acoustic Hall", "Simultaneous Translation Booths", "Orchestral Green Rooms", "Exhibition Foyer"],
    coords: { x: 420, y: 510 }
  },
  {
    id: 10,
    name: "Student Centre (The Forum)",
    category: "student-life",
    tagline: "Clubs, Events & Collaboration",
    description: "The energetic heart of student extracurricular life. Houses student union offices, creative rehearsal spaces, gaming rooms, and open collaboration lounges.",
    highlights: ["Student Union Headquarters", "Acoustic Band Practice Rooms", "TEDxAaranya Studio", "Indoor Recreation Lounge"],
    coords: { x: 635, y: 575 }
  },
  {
    id: 11,
    name: "Academic Core",
    category: "academic",
    tagline: "The Crossroads of Interdisciplinary Learning",
    description: "Central shaded rotunda and faculty office bridge that physically and intellectually joins all collegiate schools.",
    highlights: ["Cross-School Seminar Pods", "Faculty Advising Atrium", "Central Lecture Theaters"],
    coords: { x: 485, y: 480 }
  },
  {
    id: 12,
    name: "Lakeside Learning Commons",
    category: "student-life",
    tagline: "Pause. Reconnect. Discover.",
    description: "Shaded waterside gazebos and timber boardwalks equipped with weather-protected power outlets and high-speed Wi-Fi for outdoor study.",
    highlights: ["Waterside Study Decks", "Solar Pergolas with High-Speed Wi-Fi", "Contemplative Reflection Piers"],
    coords: { x: 470, y: 670 }
  },
  {
    id: 13,
    name: "Hostel Residences (North)",
    category: "residential",
    tagline: "The Grove: North Quads",
    description: "Eco-friendly residential village nestled against the northern wooded hill slopes. Offers single and double en-suite rooms with garden courtyards.",
    highlights: ["North Garden Courtyards", "Peer Study Lounges", "24/7 Security & Health Attendants"],
    coords: { x: 285, y: 300 }
  },
  {
    id: 14,
    name: "Hostel Residences (South)",
    category: "residential",
    tagline: "The Grove: South Quads",
    description: "Spacious residential blocks providing balanced, safe, and vibrant collegiate living with dining commons and fitness corners.",
    highlights: ["Panoramic Hill View Balconies", "Community Kitchens", "Recreation & Movie Rooms"],
    coords: { x: 285, y: 580 }
  },
  {
    id: 15,
    name: "Sports Complex (The Arena)",
    category: "sports",
    tagline: "Stronger Minds, Healthier Futures",
    description: "Olympic-standard athletic stadium, full-sized FIFA-grade football pitch, outdoor basketball and tennis courts, and high-performance gymnasium.",
    highlights: ["8-Lane Synthetic Athletic Track", "FIFA-Spec Grass Football Pitch", "All-Weather Tennis & Basketball Courts", "Olympic Lap Pool"],
    coords: { x: 885, y: 550 }
  },
  {
    id: 16,
    name: "Health & Wellness Centre",
    category: "wellness",
    tagline: "Holistic Health for Body & Mind",
    description: "24/7 medical infirmary, pharmacy, sports rehabilitation, mental health counseling suites, and restorative meditation rooms.",
    highlights: ["24/7 Resident Doctors & Nurses", "Mindfulness & Yoga Studios", "Licensed Psychological Counseling", "Emergency Ambulance Bay"],
    coords: { x: 865, y: 705 }
  },
  {
    id: 17,
    name: "Cafés & Dining (The Commons)",
    category: "student-life",
    tagline: "Good Food. Great Conversations.",
    description: "Central dining facility offering diverse farm-to-table culinary choices, nutritious vegan menus, artisan bakeries, and open-air seating terraces.",
    highlights: ["Multi-Cuisine Food Court", "Organic Farm-to-Table Station", "Artisanal Coffee Roasters", "Open-Air Garden Terraces"],
    coords: { x: 490, y: 840 }
  },
  {
    id: 18,
    name: "Amphitheatre",
    category: "culture",
    tagline: "Under the Open Sky",
    description: "Tiered natural stone outdoor amphitheater set against the forested hillside for open-air theater, poetry recitals, acoustic musical concerts, and student rallies.",
    highlights: ["Tiered Natural Stone Seating", "Sunset Acoustic Alignment", "Open-Air Shakespearean Productions"],
    coords: { x: 720, y: 780 }
  },
  {
    id: 19,
    name: "Open Lawns & The Harmony Quad",
    category: "green",
    tagline: "Community in Every Corner",
    description: "The expansive circular green commons at the heart of Aaranya. A gathering spot for university convocations, book fairs, and star-gazing nights.",
    highlights: ["The Harmony Central Quad", "Jacaranda & Magnolia Groves", "Starlight Film Screenings"],
    coords: { x: 530, y: 345 }
  },
  {
    id: 20,
    name: "Nature Trail & Forest Walk",
    category: "green",
    tagline: "Nature Nurtures Brighter Minds",
    description: "Winding ecological trail traversing native flora, preserved woodland groves, and hill paths for morning runs, walking seminars, and reflection.",
    highlights: ["2.5 km Preserved Woodland Trail", "Bird Sanctuary & Flora Signage", "Sunset Point Outlook"],
    coords: { x: 785, y: 220 }
  },
  {
    id: 21,
    name: "Sustainability Zone",
    category: "research",
    tagline: "Greener Solutions for Stronger Tomorrows",
    description: "Live ecological research zone featuring a 1.2 MW campus solar farm, organic botanical research beds, rainwater harvesting lakes, and composting center.",
    highlights: ["1.2 MW Solar Photovoltaic Farm", "Rainwater Bio-Filtration Basins", "Medicinal Plant Botanical Arboretum"],
    coords: { x: 295, y: 790 }
  }
];

document.addEventListener('DOMContentLoaded', () => {
  initCampusMap();
});

function initCampusMap() {
  const mapSvg = document.getElementById('campusMapSvg');
  const directoryContainer = document.getElementById('landmarksList');
  const detailCard = document.getElementById('landmarkDetailCard');
  const filterButtons = document.querySelectorAll('.map-filter-btn');

  if (!directoryContainer) return;

  renderDirectoryList(CAMPUS_LANDMARKS);
  renderSvgMarkers(CAMPUS_LANDMARKS);

  // Category Filtering
  filterButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      filterButtons.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      const filterCat = btn.getAttribute('data-category');
      const filtered = filterCat === 'all' 
        ? CAMPUS_LANDMARKS 
        : CAMPUS_LANDMARKS.filter(item => item.category === filterCat);

      renderDirectoryList(filtered);
      renderSvgMarkers(filtered);
    });
  });

  // Select the first landmark by default
  selectLandmark(CAMPUS_LANDMARKS[0]);
}

function renderDirectoryList(landmarks) {
  const directoryContainer = document.getElementById('landmarksList');
  if (!directoryContainer) return;

  directoryContainer.innerHTML = '';

  if (landmarks.length === 0) {
    directoryContainer.innerHTML = '<p style="padding: 1.5rem; color: #4a554e;">No landmarks found in this category.</p>';
    return;
  }

  landmarks.forEach(lm => {
    const item = document.createElement('div');
    item.className = 'landmark-item';
    item.setAttribute('data-id', lm.id);
    item.innerHTML = `
      <div class="landmark-badge">${lm.id}</div>
      <div class="landmark-info">
        <h4>${lm.name}</h4>
        <span>${lm.tagline}</span>
      </div>
    `;

    item.addEventListener('click', () => {
      selectLandmark(lm);
    });

    directoryContainer.appendChild(item);
  });
}

function renderSvgMarkers(landmarks) {
  const markersGroup = document.getElementById('svgMarkersGroup');
  if (!markersGroup) return;

  markersGroup.innerHTML = '';

  landmarks.forEach(lm => {
    const g = document.createElementNS('http://www.w3.org/2000/svg', 'g');
    g.setAttribute('class', 'map-pin');
    g.setAttribute('data-id', lm.id);
    g.style.cursor = 'pointer';

    g.innerHTML = `
      <circle cx="${lm.coords.x}" cy="${lm.coords.y}" r="15" fill="#163024" stroke="#ffffff" stroke-width="2.5" />
      <text x="${lm.coords.x}" y="${lm.coords.y + 4.5}" text-anchor="middle" fill="#f8faf7" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" font-weight="700">${lm.id}</text>
    `;

    g.addEventListener('click', () => {
      selectLandmark(lm);
    });

    markersGroup.appendChild(g);
  });
}

function selectLandmark(landmark) {
  // Highlight in directory
  document.querySelectorAll('.landmark-item').forEach(el => {
    el.classList.toggle('selected', parseInt(el.getAttribute('data-id')) === landmark.id);
  });

  // Highlight in SVG
  document.querySelectorAll('.map-pin').forEach(el => {
    const circle = el.querySelector('circle');
    if (circle) {
      if (parseInt(el.getAttribute('data-id')) === landmark.id) {
        circle.setAttribute('fill', '#b87d4b');
        circle.setAttribute('r', '18');
        circle.setAttribute('stroke', '#ffffff');
        circle.setAttribute('stroke-width', '3');
      } else {
        circle.setAttribute('fill', '#163024');
        circle.setAttribute('r', '15');
        circle.setAttribute('stroke', '#ffffff');
        circle.setAttribute('stroke-width', '2.5');
      }
    }
  });

  // Update Detail Card
  const detailCard = document.getElementById('landmarkDetailCard');
  if (!detailCard) return;

  detailCard.innerHTML = `
    <div style="background-color: #faf8f5; border: 1px solid rgba(22,48,36,0.12); padding: 1.75rem; border-radius: 4px;">
      <div style="display: flex; align-items: center; gap: 0.75rem; margin-bottom: 0.75rem;">
        <span class="landmark-badge" style="width: 34px; height: 34px; font-size: 0.95rem; background-color: #b87d4b;">${landmark.id}</span>
        <div>
          <span class="eyebrow" style="margin-bottom: 0;">ZONE #${landmark.id} · ${landmark.category.toUpperCase()}</span>
          <h3 style="font-size: 1.45rem; line-height: 1.2;">${landmark.name}</h3>
        </div>
      </div>
      <p style="font-style: italic; color: #b87d4b; font-size: 0.9rem; margin-bottom: 1rem;">“${landmark.tagline}”</p>
      <p style="color: #4a554e; font-size: 0.92rem; line-height: 1.6; margin-bottom: 1.25rem;">${landmark.description}</p>
      
      <h5 style="font-size: 0.8rem; text-transform: uppercase; letter-spacing: 0.12em; color: #163024; margin-bottom: 0.6rem; font-weight: 700;">Key Features & Facilities:</h5>
      <ul style="margin-bottom: 1.5rem;">
        ${landmark.highlights.map(h => `<li style="font-size: 0.85rem; color: #191e1b; padding: 0.25rem 0; display: flex; align-items: center; gap: 0.5rem;"><svg viewBox="0 0 8 8" width="6" height="6" style="fill: #b87d4b; flex-shrink: 0;"><circle cx="4" cy="4" r="3"/></svg> ${h}</li>`).join('')}
      </ul>

      <a href="contact.html?visit=${landmark.id}" class="btn btn-secondary" style="width: 100%; text-align: center; font-size: 0.78rem;">Schedule Campus Tour Visit</a>
    </div>
  `;
}
