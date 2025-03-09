# AVD Ticketing System

## Overview
The AVD Ticketing System is a web application designed to manage ticketing operations efficiently. It provides interfaces for both managers and super admins to handle user data and customize access levels.

## Project Structure
```
avd-tickiting-system
├── manager.html        # Interface for managing admin and manager data
├── superadmin.html     # Interface for super admin to customize access
└── README.md           # Documentation for the project
```

## Features
- **Manager Management**: 
  - Add, edit, delete, and restore manager data.
  - View manager details in a structured table format.
  - Sidebar navigation for easy access to different sections.

- **Super Admin Customization**:
  - Options to customize access for admins and managers.
  - Sections for SCT, Members, and MC type.
  - Horizontal branch layout for viewing different customization options.

## Setup Instructions
1. Clone the repository:
   ```
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```
   cd avd-tickiting-system
   ```
3. Open `manager.html` or `superadmin.html` in a web browser to view the interfaces.

## Usage Guidelines
- Ensure that the server is running to fetch data for managers and super admins.
- Use the sidebar in `manager.html` for navigation between different management sections.
- In `superadmin.html`, utilize the customization options to manage access levels effectively.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.