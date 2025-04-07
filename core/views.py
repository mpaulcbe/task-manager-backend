from django.http import HttpResponse

def homepage(request):
    return HttpResponse("""
        <html>
            <head>
                <title>Task Manager API</title>
                <style>
                    body {
                        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                        background: linear-gradient(to right, #e3f2fd, #ffffff);
                        display: flex;
                        flex-direction: column;
                        align-items: center;
                        justify-content: center;
                        height: 100vh;
                        margin: 0;
                    }
                    h1 {
                        font-size: 2.5em;
                        color: #0d47a1;
                        margin-bottom: 0.5em;
                    }
                    p {
                        font-size: 1.2em;
                        margin-bottom: 1em;
                        color: #424242;
                    }
                    .btn-group {
                        display: flex;
                        gap: 1rem;
                    }
                    .btn {
                        background-color: #1976d2;
                        color: white;
                        padding: 0.75rem 1.5rem;
                        border: none;
                        border-radius: 8px;
                        text-decoration: none;
                        font-size: 1rem;
                        transition: background-color 0.3s ease;
                    }
                    .btn:hover {
                        background-color: #0d47a1;
                    }
                </style>
            </head>
            <body>
                <h1>Welcome to the Task Manager API 🚀</h1>
                <p>Select an option below to get started:</p>
                <div class="btn-group">
                    <a href="/api/" class="btn">Explore API</a>
                    <a href="/admin/" class="btn">Admin Panel</a>
                    <a href="http://localhost:4200" class="btn">Frontend App</a>
                </div>
            </body>
        </html>
    """)
