const fs = require('fs');

function extractSection(content, sectionHeading) {
  const regex = new RegExp(`${sectionHeading}\\n([^#]+)`, 'i');
  const match = content.match(regex);
  return match ? match[1].trim() : '';
}

function main() {
  const title = process.env.INPUT_TITLE;
  const body = process.env.INPUT_BODY;
  const originRepoUrl = `${process.env.GITHUB_SERVER_URL}/${process.env.GITHUB_REPOSITORY}`;

  const bugDescription = extractSection(body, "### 1. **Bug/Vulnerability Description**");
  const hardwareSoftwareSpecs = extractSection(body, "### 2. **Hardware and Software Specifications**");
  const stepsToReproduce = extractSection(body, "### 3. **Steps to Reproduce**");
  const impactAnalysis = extractSection(body, "### 4. **Impact Analysis**");
  const codeFixSubmission = extractSection(body, "### 5. **Code Fix Submission**");
  const chooseTheRightLabel = extractSection(body, "### 6. **Choose the Right Label**");
  const additionalContext = extractSection(body, "### 7. **Additional Context**");

  const bodyWithLink = `**Bug/Vulnerability Description:**\n${bugDescription}\n\n**Hardware and Software Specifications:**\n${hardwareSoftwareSpecs}\n\n**Steps to Reproduce:**\n${stepsToReproduce}\n\n**Impact Analysis:**\n${impactAnalysis}\n\n**Code Fix Submission:**\n${codeFixSubmission}\n\n**Choose the Right Label:**\n${chooseTheRightLabel}\n\n**Additional Context:**\n${additionalContext}\n\nComments are not being updated\nOriginal Issue can be found [here](${originRepoUrl})`;

  console.log(bodyWithLink);
}

main();
