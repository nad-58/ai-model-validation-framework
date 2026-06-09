# Public Release Checklist

Use this checklist before changing repository visibility from private to public.

## Content and confidentiality

- [ ] No client, customer, employer, patient, participant, or supplier confidential information
- [ ] No internal assessment reports, audit evidence, screenshots, meeting notes, or proprietary procedures
- [ ] No personal email addresses, phone numbers, home addresses, or other unnecessary personal data
- [ ] No API keys, passwords, tokens, private keys, certificates, or environment files
- [ ] No copyrighted third-party material copied beyond permitted quotation or attribution
- [ ] All datasets and examples are synthetic, public, or clearly licensed for redistribution

## Code and testing

- [ ] Unit tests pass
- [ ] Every example script runs successfully
- [ ] Source files compile successfully
- [ ] The package builds successfully
- [ ] Package metadata passes validation
- [ ] Input validation and failure behaviour are documented

## Repository hygiene

- [ ] `.gitignore` excludes generated files and local environments
- [ ] Full Git history has been scanned for secret-like content
- [ ] README links and file paths are correct
- [ ] Licence is present and appropriate
- [ ] Security policy is present
- [ ] Repository description and topics contain no confidential wording

## Public positioning

- [ ] README states that examples are synthetic and generic
- [ ] README includes limitations and does not imply certification or regulatory approval
- [ ] Acceptance criteria are clearly described as illustrative
- [ ] No employer or customer endorsement is implied

## Final visibility change

Only change visibility after the public-readiness pull request is merged and all GitHub Actions checks pass. After making the repository public, open it in a signed-out browser session and confirm that only intended content is visible.
