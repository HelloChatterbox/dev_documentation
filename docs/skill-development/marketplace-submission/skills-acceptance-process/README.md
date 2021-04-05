---
description: >-
  The Skills Acceptance Process outlines how Skills are tested, reviewed,
  deployed and promoted through the Chatterbox Marketplace.
---

# Skills Acceptance Process

It is vital that Chatterbox Skills exhibit high quality, and are well tested to encourage adoption, and ongoing development of the platform. This process contributes to that goal by providing a structured framework to follow to ensure repeatable outcomes.

## Overview

The process consists of 6 stages:

1. [Submitting your Skill](./#1-submitting-your-skill)
2. [Automatic testing](./#2-automatic-testing-of-skills)
3. [Review by Skill Testing Team](./#3-review-by-skill-testing-team)
   * Code Review
   * Information Review
   * Functional Review
4. [Review by Chatterbox AI](./#4-review-by-chatterbox-ai)
5. [Deployment](./#5-deployment)
6. [Promotion](./#6-promotion)

## Submission

### 1. Submitting your Skill

Before submitting your Skill we assume you have:

* Create your README.md using the [Skill Meta Editor](https://chatterbox.ai/skill-meta-editor). We also have some [additional tips for a great README](../skill-readme-md.md).
* Personally tested your Skills functionality to ensure it is working as expected. For a detailed testing overview, see stage three below.
* It is also a great idea to post a link to you Skill in the [Skill Feedback category of the Forums](https://community.chatterbox.ai/c/skill-feedback) to let others test your Skill on different platforms. This is encouraged but not required to submit your Skill to the Marketplace.
* Ensure any Python or other packages required to run your Skill are included in your requirements.txt or equivalent.
* Run the [automated testing](../../voight-kampff/automatic-testing.md) on your own machine using the command:

  `chatterbox-skill-testrunner /opt/chatterbox/skills/your-skill-directory`

When you are satisfied your Skill is ready, submit it for formal review by running:

```text
chatterbox-msk submit /opt/chatterbox/skills/your-skill-directory
```

If you don't have the chatterbox-msk command available, you can manually activate the Chatterbox virtual environment and run `msk`

```text
source ~/chatterbox-core/.venv/bin/activate
msk submit /opt/chatterbox/skills/your-skill-directory
```

This will upload the Skill to Github if it isn’t already, and generate a pull request to add your Skill as a [Git submodule](https://gist.github.com/gitaarik/8735255) to the [Chatterbox Skills Repo](https://github.com/ChatterboxAI/chatterbox-skills).

### 2. Automatic Testing of Skills

We have developed an Integration Test Runner that assists you in writing tests that can be executed at both an **Intent** and a **Skill** level. [Learn more about Automatic Testing of your Chatterbox Skill](../../voight-kampff/).

This automated testing is run as soon as you submit your Skill to the Chatterbox-Skills repo, and with each major release of Chatterbox-core.

## Review

### 3. Review by Skill Testing Team

The Skill Testing Team is made up of experienced Chatterbox Community Members and Chatterbox AI Staff. One of the team’s responsibilities is to ensure Skills meet minimum quality, technical and functional standards to maintain the user experience with every Skill in the Marketplace. When a Skill Author submits a Skill to the [Chatterbox Skills Repo](https://github.com/ChatterboxAI/chatterbox-skills), the Skill Testing Team conducts three reviews.

a. [Code Review](skills-review-code-template.md) - ensuring the code is stable and secure  
b. [Information Review](skills-review-information-template.md) - ensuring all info is accurate and understandable  
c. [Functional Review](skills-review-functional-template.md) - ensuring the experience of using the Skill is intuitive

The Skill Author will receive feedback and may need to solve issues identified in these reviews before it will be approved.

### 4. Review by Chatterbox AI

The purpose of this step is for a Chatterbox AI staff member to do a final check of a Skill. The staff member will be looking for:

* Profanity – does the Skill contain profanity?
* Sexually explicit material – does the Skill contain sexually explicit references or language?
* Offensive or pejorative language – does the Skill contain offensive references or language, for example language that is homo-, trans-, or bi-phobic, racist, religiously intolerant etc.
* Other content that has the ability to damage the reputation of the Chatterbox platform.

If any such content is found, the PR for the Skill to be added to the [Chatterbox Skills Repo](https://github.com/ChatterboxAI/chatterbox-skills) will be tagged as flagged and escalated for review by Chatterbox AI senior management, who will then make a determination on whether the Skill will be pulled into the Chatterbox repo.

## What happens next?

### 5. Deployment

If the Skill passes all reviews, it will then be merged into the [Chatterbox Skills Repo](https://github.com/ChatterboxAI/chatterbox-skills). Once it is merged, the Skill becomes available for any Chatterbox Device to install using voice commands.

### 6. Promotion

Once a Skill is deployed, the following measures may be taken by Chatterbox Staff promote the Skill to the Chatterbox Community. The Skill Author is of course welcome to do additional promotion of their own.

* Listing on the [Chatterbox Skills Marketplace](https://market.chatterbox.ai/)
* Shoutout in Chatterbox Newsletter
* Notification on [Chatterbox Forum](https://community.chatterbox.ai/)
* Notification in [~Skills Channel on Chatterbox Chat](https://chat.chatterbox.ai/community/channels/skills)
* Notification through Chatterbox social media

We also encourage the Skill Author to make a short video of the Skill in action to aid in promotion.

## Frequently Asked Questions

### What are the labels used on the `chatterbox-skills` repo?

While a **Skill** is undergoing review, there are several _labels_ used on the PR to help indicate status.

* **approved** - This Skill is ready to be merged to the current branch, ie 18.02
* **needs validation** This Skill needs validating by a Community Member and cannot be validated by Skills Team
* **new** This is a new Skill \(rather than an update to an existing Skill\)
* **override autotester** The Skills Team has determined that acceptance of this PR should override the AutoTester
* **under review** This Skill is being reviewed by the Skills Team
* **update** This Skill is an update to an existing Skill
* **waiting** This PR or Issue is waiting on the Skill Author to respond

![Chatterbox Skills Repo labels](https://chatterbox.ai/wp-content/uploads/2018/06/chatterbox-skils-repo-labels.png)

### What happens if the Skill Testing Team can't test the Skill?

Often, Skills will have niche requirements. For example, they may be dependent on third party APIs or the installation of entire software stacks. In this case, it is impractical for the Skill Management Team to test the Skill.

Instead, the Skill Management Team will seek assistance from the Community, and will invite the Community member who volunteers to add comments to the Pull Request. Then, the Skills Management Team will review the comments and merge or decline the PR.

### I am keen to help test Skills, how do I get involved?

Head to our [contribute page](https://chatterbox.ai/contribute/#suggest-and-test-skills) to submit an application and see the many other ways you can be involved.

Our Skills Testing Team are a fantastic group of community members who ensure that all Skills are secure, stable, accurate, and intuitive. The team has members with a range of skills and communicate through a private channel on [chat.chatterbox.ai](https://chat.chatterbox.ai/).

