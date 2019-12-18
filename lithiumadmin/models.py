from django.db import models


class Customer(models.Model):
    ON_PREMISE = "ONP"
    HOSTED = "HOS"
    SAAS = "SAA"
    HOSTING_CHOICES = [(ON_PREMISE, "On-Premise"), (HOSTED, "Hosted"), (SAAS, "SaaS")]

    name = models.CharField(max_length=50, unique=True)
    prod_hosting = models.CharField(max_length=3, choices=HOSTING_CHOICES, default=SAAS)
    prod_version = models.CharField(max_length=10)

    def __str__(self):
        on_prem = "# " if self.prod_hosting == Customer.ON_PREMISE else ""
        return f"{on_prem}{self.name}"


class KnownBug(models.Model):
    jira_case = models.CharField(max_length=20, unique=True)
    description = models.TextField()
    affected_versions = models.CharField(max_length=100)
    fix_versions = models.CharField(max_length=100, default="Not fixed")

    def __str__(self):
        return self.jira_case


class Case(models.Model):
    QUEUED = "QUE"
    IN_PROGRESS = "INP"
    NOT_LITHIUM = "NOT"
    CLOSED = "CLO"
    STATUS_CHOICES = [
        (QUEUED, "Queued with Lithium"),
        (IN_PROGRESS, "In Progress"),
        (NOT_LITHIUM, "Waiting on another Team"),
        (CLOSED, "Closed / Resolved"),
    ]

    CRITICAL = "CRI"
    HIGH = "HI"
    MEDIUM = "MED"
    LOW = "LOW"
    PRIORITY_CHOICES = [
        (CRITICAL, "Critical"),
        (HIGH, "High"),
        (MEDIUM, "Medium"),
        (LOW, "Low"),
    ]

    SEV1 = "SEV1"
    SEV2 = "SEV2"
    SEV3 = "SEV3"
    NONE = "SEVN"
    SEVERITY_CHOICES = [
        (SEV1, "Severity 1"),
        (SEV2, "Severity 2"),
        (SEV3, "Severity 3"),
        (NONE, "None"),
    ]

    customer = models.ForeignKey(Customer, related_name="customer_cases", on_delete=models.CASCADE)

    title = models.CharField(max_length=100)
    salesforce_case = models.CharField(max_length=10, unique=True)

    date_entered = models.DateField(auto_now_add=True)
    date_requested = models.DateField()

    status = models.CharField(max_length=3, choices=STATUS_CHOICES, default=QUEUED)
    priority = models.CharField(max_length=3, choices=PRIORITY_CHOICES, default=MEDIUM)
    severity = models.CharField(max_length=4, choices=SEVERITY_CHOICES, default=SEV3)

    is_billable = models.BooleanField(default=False)
    project_code = models.CharField(max_length=20, blank=True)

    files_location = models.CharField(max_length=300, blank=True)

    customer_notes = models.TextField()
    analyst_notes = models.TextField(blank=True)
    developer_notes = models.TextField(blank=True)
    my_notes = models.TextField(blank=True)

    associated_bug = models.ForeignKey(KnownBug, related_name="bug_cases", on_delete=models.PROTECT, blank=True, null=True)
    report_me = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.salesforce_case}: ({self.customer.name}) - {self.title}"
