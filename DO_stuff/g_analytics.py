import os

def os_env_err():
  print("""OS ENV ERROR
Please set the following environment variables:

GOOGLE_ANALYTICS_VIEW_ID

Reference file: /home/devel/Documents/env_vars/free_books_env_vars.txt
""")
  exit()

try:
  g_analytics_view_id = os.getenv('GOOGLE_ANALYTICS_VIEW_ID')
except:
  os_env_err()
  
g_analytics_template_p1 = "    <!-- Google tag (gtag.js) -->\n    <script async src=\"https://www.googletagmanager.com/gtag/js?id="+g_analytics_view_id+"\"></script>"

g_analytics_template_p2 = """
    <script>
        window.dataLayer = window.dataLayer || [];
        function gtag(){dataLayer.push(arguments);}
        gtag('js', new Date());
"""

g_analytics_template_p3 = "        gtag('config', '"+g_analytics_view_id+"');"

g_analytics_template_p4 = """
    </script>
"""

g_analytics_template = g_analytics_template_p1+g_analytics_template_p2+g_analytics_template_p3+g_analytics_template_p4