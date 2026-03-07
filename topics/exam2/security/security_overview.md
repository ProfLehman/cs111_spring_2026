# Security Overview

*CS 111 – Introduction to Computer Science*  
Dr. Jeff Lehman  
Huntington University

---

# What Can Go Wrong?

![what can go wrong](./images/go_wrong.png)

Computer systems can fail or lose data for many reasons.

Common causes include:

- **Human Error**
  - Accidental deletion of files
  - Incorrect configuration
- **Electricity Problems**
  - Power outages
  - Power surges
- **Hardware Failure**
  - Hard drive crashes
  - Component wear
  - MTBF — *Mean Time Between Failures*
- **Natural Disasters**
  - Fire
  - Flood
  - Tornado
- **Software Failure**
  - Bugs or crashes
- **Malicious Software**
  - Viruses
  - Spyware
  - Ransomware

---

# Computer Viruses

![Computer Virus](./images/virus.png)

A **computer virus** is a malicious program that:

- Destroys or alters data or programs
- Causes system problems or annoyance
- **Replicates itself**
- Requires a **host file or program**
- Is intentionally created by humans

### Why Are Viruses Created?

Common motivations include:

- Power
- Prestige
- Thrill

---

# Types of Viruses

### Macro Virus

Uses commands inside applications such as:

- Microsoft Word
- Excel
- Outlook

---

### Trojan Horse

A program that **pretends to be legitimate software** but performs hidden malicious actions.

---

### Time Bomb

Malicious code that activates at a **specific date or time**.

---

### Worm

A self-replicating program that spreads through networks **without needing a host program**.

---

# Virus Protection

### Anti-Virus Software

Examples include:

- Norton
- Sophos
- AVG
- Avast
- McAfee

These programs:

- Detect malware
- Remove malicious programs
- Monitor suspicious activity

---

### Safe Email Practices

Be cautious when opening email attachments.

Always:

- Know the **sender**
- Know the **content**
- Avoid unexpected attachments

---

# Spyware, Adware, and Malware

![Malware Types](images/spyware.png)

### Spyware

Software that secretly **collects personal data** about users.

Examples:

- Browsing habits
- Passwords
- Personal information

---

### Adware

Software that **displays advertisements** on a computer.

Often bundled with free software.

---

### Malware

A general term for **malicious software** that disrupts or damages a system.

---

# Anti-Spyware Tools

Programs designed specifically to remove spyware.

Examples include:

- Ad-Aware
- SpyBot Search & Destroy
- CCleaner

Many modern antivirus programs include **anti-spyware protection**.

### Safety Tip

Be cautious of **free software downloads**.

They may install unwanted programs.

---

# Ransomware

**Ransomware** encrypts files on a computer or network.

Attackers demand **payment (a ransom)** to:

- Restore access to files
- Prevent data from being publicly released

Ransomware attacks often target:

- Businesses
- Hospitals
- Government systems
- Universities

---

# Phishing and Hoaxes

![Phishing](images/phishing.png)

### Phishing

An attempt to steal personal information using **fake emails or websites**.

These messages often look like they come from:

- Banks
- PayPal
- Amazon
- Universities

---

### Hoax Emails

Messages that appear believable but are **false**.

They often encourage users to:

- Forward the message
- Click suspicious links
- Provide personal information

---

### Best Practice

Before responding:

- Verify the message
- Check the sender
- Do not reply to suspicious emails

---

# Risk Management

Security decisions should reflect the **value of the data being protected**.

Example:

| Data Type | Security Needed |
|-----------|----------------|
| Homework files | Low |
| Personal photos | Medium |
| Financial data | High |
| Company customer database | Very High |

---

# Security Measures

![Security Measures](images/security_measures.png)

Common ways to protect systems include:

### Physical Security

- Locked rooms
- Secure server locations

---

### Authentication

- Passwords
- User IDs
- Biometrics (fingerprint, face recognition)

---

### Access Control

Restrict who can access systems or data.

Examples:

- Administrator privileges
- File permissions

---

### Encryption

Protects data by converting it into unreadable form.

Only authorized users can decrypt it.

---

### Hardware Redundancy

Extra hardware components provide backup if one fails.

Example:

- RAID storage systems

---

### Backups

Copies of important data stored separately from the original.

---

### Disaster Recovery Plans

Procedures to restore systems after a failure or disaster.

---

# Password Best Practices

Strong passwords should:

- Avoid dictionary words
- Include **upper and lower case letters**
- Include **symbols or numbers**
- Be **longer**

Long passwords are much harder to crack.

---

### Password Managers

Tools that securely store passwords.

Examples:

- LastPass
- 1Password
- KeePass
- Dashlane

These allow users to maintain **unique passwords for each account**.

---

# XKCD Password Example

![XKCD Password](images/xkcd_password.png)

A long passphrase can be easier to remember and harder to guess.

Example:

```

correct horse battery staple

```

This type of password has **high entropy** but remains easy for humans to remember.

---

# Backup Planning

A good backup plan should answer several questions.

### What files should be backed up?

- Documents
- Photos
- Programs
- Settings

---

### When should backups occur?

- Daily
- Weekly
- Monthly

---

### Where should backups be stored?

Examples:

- USB drive
- External hard drive
- Network storage
- Cloud storage

---

### Where should backup media be kept?

Possible locations include:

- File drawer
- Lockbox
- Another building
- Cloud storage

---

# Types of Backups

There are three common backup methods.

---

## Full Backup

![Full Backup](images/full_backup.png)

A **full backup** copies all files every time.

Advantages:

- Simple restore process

Disadvantages:

- Requires large storage space
- Takes longer to complete

---

## Differential Backup

![Differential Backup](images/differential_backup.png)

Copies **all files changed since the last full backup**.

Advantages:

- Faster than full backup
- Restore requires only two backups

---

## Incremental Backup

![Incremental Backup](images/incremental_backup.png)

Copies **files changed since the last backup**.

Advantages:

- Very fast backups
- Requires minimal storage

Disadvantages:

- Restoring requires multiple backup sets

---

# Cloud Backups

Cloud storage services often use **incremental backups**.

Examples include:

- iCloud
- Dropbox
- OneDrive
- Google Drive

Process:

1. Initial **full backup**
2. Only **changes** are uploaded afterward

This allows systems to **roll back to earlier versions**.

---

# The 3-2-1 Backup Strategy

A widely recommended rule for backups.

### 3 Copies of Data

- Original file
- Two backup copies

---

### 2 Local Copies

Stored on different media.

Example:

- Laptop
- External drive

---

### 1 Off-Site Copy

Stored at another location.

Examples:

- Cloud storage
- Office server
- Family member’s house

---

# The 3-2-1-1-0 Backup Strategy

An improved version of the 3-2-1 rule.

Adds:

- **1 Offline Backup**
  - Protects against ransomware
- **0 Backup Errors**
  - Verify backups regularly

---

# Cloud Storage Example: OneDrive

![OneDrive](images/onedrive.png)

Huntington University students receive:

**5 TB of free cloud storage**

To access:

1. Login to HU email
2. Open the Office 365 app launcher
3. Select **OneDrive**

---

# Disaster Recovery

A **disaster recovery plan** describes how an organization restores systems after a disaster.

Possible disasters include:

- Cyberattacks
- Hardware failures
- Fires
- Floods
- Power outages

A recovery plan may include:

- Data restoration procedures
- Backup systems
- Emergency contacts
- System restoration steps

---

# Final Question

![Disaster Plan](images/disaster_plan.png)

**What is your disaster recovery plan?**

Every organization — and every individual — should have one.
```

-- end --
