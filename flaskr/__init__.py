from flask import Flask, request, jsonify
from flask_cors import CORS
app = Flask(__name__)
# Enable Cross-Origin Resource Sharing (CORS) for the entire API
CORS(app)

# Add CORS-related headers to every response
@app.after_request
def after_request(response):
    # Allow the client to send these headers
    response.headers.add('Access-Control-Allow-Headers','Content-Type, Authorization')

    # Explicitly allow common HTTP methods for CORS preflight requests
    response.headers.add('Access-Control-Allow-Methods','GET, POST, PATCH, DELETE, OPTIONS')
    return response

# Sample data set (in practice, this would come from a database)
ITEMS = [ "apple", "banana", "carrot", "donut", "egg",
   "fig", "grape", "honey", "ice cream", "juice"]

@app.route('/items')
def get_items():
    # Read pagination parameters from the query string
    # Example: /items?page=2&per_page=3
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 3, type=int)

    # Calculate slice boundaries
    start = (page - 1) * per_page
    end = start + per_page

    # Select only the items for the requested page
    paginated_items = ITEMS[start:end]

    return jsonify({
        'page': page,
        'per_page': per_page,
        'total_items': len(ITEMS),
        'items': paginated_items
    })

if __name__ == '__main__':
    app.run(debug=True)