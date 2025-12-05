const form = document.getElementById("analyze-form");
const statusEl = document.getElementById("status");
const resultSection = document.getElementById("result-section");
const resultOutput = document.getElementById("result-output");
const analyzeBtn = document.getElementById("analyze-btn");

form.addEventListener("submit", async (event) => {
  event.preventDefault();

  statusEl.classList.remove("error");
  statusEl.textContent = "";
  resultSection.classList.add("hidden");
  resultOutput.textContent = "";

  const resumeFile = document.getElementById("resume").files[0];
  const jobFile = document.getElementById("job").files[0];

  if (!resumeFile || !jobFile) {
    statusEl.textContent = "Please select both files.";
    statusEl.classList.add("error");
    return;
  }

  const formData = new FormData();
  formData.append("resume", resumeFile);
  formData.append("job", jobFile);

  try {
    analyzeBtn.disabled = true;
    statusEl.textContent = "Analyzing your resume and job description...";

    const response = await fetch("/api/analyze", {
      method: "POST",
      body: formData,
    });

    if (!response.ok) {
      const text = await response.text();
      throw new Error(text || `Server error (${response.status})`);
    }

    const aiText = await response.text();

    statusEl.textContent = "Done!";
    resultOutput.textContent = aiText || "No response from AI.";
    resultSection.classList.remove("hidden");
  } catch (err) {
    console.error(err);
    statusEl.textContent = `Error: ${err.message}`;
    statusEl.classList.add("error");
  } finally {
    analyzeBtn.disabled = false;
  }
});
