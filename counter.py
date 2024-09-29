from django.db import models
from nanodjango import Django

  
app = Django()

@app.api.get("/count")
def hello(request):
    return {"count": CountLog.objects.count()}

@app.admin(
    list_display=["id", "timestamp"],
    readonly_fields=["timestamp"],
)
class CountLog(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)

@app.route("/")
def count(request):
    CountLog.objects.create()
    return f"<p>Number of page loads: {CountLog.objects.count()}</p>"
  

