const notesGrid = document.getElementById("notesGrid");
const emptyState = document.getElementById("emptyState");
const statusBadge = document.getElementById("statusBadge");
const form = document.getElementById("noteForm");

async function refreshHealth() {
  try {
    const res = await fetch("/health");
    const ok = res.ok;
    statusBadge.textContent = ok ? "API OK" : "API down";
    statusBadge.className = `badge ${ok ? "bg-success" : "bg-danger"}`;
  } catch (e) {
    statusBadge.textContent = "API down";
    statusBadge.className = "badge bg-danger";
  }
}

function renderNotes(notes) {
  notesGrid.innerHTML = "";
  notes.forEach((note) => {
    const col = document.createElement("div");
    col.className = "col-12 col-md-6";
    col.innerHTML = `
      <div class="card card-note shadow-sm h-100">
        <div class="card-body">
          <h5 class="card-title mb-1">${note.title}</h5>
          <p class="card-text mb-2">${note.body}</p>
          <small>ID: ${note.id}</small>
        </div>
      </div>`;
    notesGrid.appendChild(col);
  });
  emptyState.style.display = notes.length ? "none" : "block";
}

async function loadNotes() {
  const res = await fetch("/notes");
  const data = await res.json();
  renderNotes(data);
}

form.addEventListener("submit", async (e) => {
  e.preventDefault();
  const formData = new FormData(form);
  const payload = Object.fromEntries(formData.entries());
  await fetch("/notes", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload),
  });
  form.reset();
  await loadNotes();
});

refreshHealth();
loadNotes();