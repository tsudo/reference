# AD_DesignRecommendations

Original format: `docx`

# Active Directory Recommendations for Security and Compliance

The following recommendations are intended to establish and sustain an Active Directory environment that reduces the attack surface of the organization and provides for granular and auditable access controls.

## Standards

* Establish and document a naming convention for OUs, Groups, and Users.
* Define which user fields should be completed for each user (e.g., Department, Manager, Description, Phone Number). Document this in User Setup Checklist.
* File and folder access permissions should not be granted to any individual user. All access controls should be enabled and restricted via a folder permissions group or role-based security group.
* Establish templates for new users. This template should be a disabled user with placeholders in the required user fields that will be used, via copy, to create new personnel accounts. Each major user role or type (e.g., Finance, Admin, Clinical) should have a user template.

## Best Practices

1. Apply Security GPOs to the domain root to ensure universal application of account security and auditing settings.
   1. Security settings should be set to overwrite locally defined settings and applied to workstation and servers.
2. Utilize user fields to designate accounts as employees or contractors. This is in addition to OU segmentation to allow for visibility directly in access control reports and queries.
3. OU segmentation should be primarily focused on type to enable more granular GPO enforcement.
   1. Computer OUs should be organized by type.
      1. Servers
         1. Domain Controllers
         2. Member Servers
            1. Web / Application / File
      2. Computers
         1. Desktops
         2. Laptops
   2. User OUs should be organized by type.
      1. Employee / Contractor / Admins / Service Accounts
         1. For Service Accounts apply policy to disable interactive login
         2. For Admin Accounts apply policy to disable logon as service/batch
      2. Also create OU for “Disabled Users”
4. Security group segmentation should be primarily focused on roles to enable appropriate and auditable access controls (i.e. Folder/File Permissions)
   1. For Example: IT / Finance/ Clinical
   2. Create permission groups for Company/Departmental shares that segment read and write functions. User security groups should then be added to these Access Control groups. This is especially important in designating access to sensitive data shares. This model provides for enhanced auditing and prevents needing to change permissions to the actual folder beyond initial setup.
5. Least Privilege:
   1. The domain admin account should be set to a long and complex password. Beyond creating specific admin accounts, it should never be used again.
   2. No user should use an admin account for day-to-day activity. Each IT administrator should have a normal permissions account and a second administrator account created for that user.
   3. Delegate appropriate admin permissions. No user administrator account should be in Domain Admins Group permanently. If Domain Admin is needed, then the account should be moved into that Group for the duration of the function and then removed.
   4. Deploy LAPS to manage local administrator passwords.
