#!/usr/bin/python3

import json

with open('resume.json', 'r', encoding='utf-8') as file:
  data = json.load(file)

MD_FILE = f'{data['name'].replace(' ', '')}-resume.md'.lower()

with open(MD_FILE, 'w', encoding='utf-8') as md:
  md.write(f'# {data['name']}\n')
  md.write(f'**{data['current_job_title']}**\n\n')

  for key, value in data['contact'].items():
    md.write(f'- **{key.capitalize()}**: {value}\n')
  md.write('\n')

  md.write('## Professional Summary\n')
  md.write(f'{data['professional_summary']}\n\n')

  md.write('## Technical Skills\n')
  md.write(', '.join(data['technical_skills']) + '\n\n')

  md.write('## Work Experience\n\n')
  for job in data['work_experience']:
    md.write(f'### **{job['title']} | {job['company']} | {job['location']}** | *({job['date']})*')
    md.write(f'\n')
    for duty in job['duties']:
      md.write(f'- {duty}\n')
    md.write('\n')

  md.write('## Education\n')
  for edu in data['education']:
    md.write(f'- {edu}\n')

print(f'✅ Markdown generated: {MD_FILE}')
