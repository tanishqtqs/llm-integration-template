from flask import Blueprint, request, jsonify
from .services.openai_services.openai_handlers import OpenAIService
from .services.gemini_services.gemini_handlers import GeminiService

bp = Blueprint('routes', __name__)
gpt = OpenAIService()
gem = GeminiService()
@bp.route('/query-llm', methods=['POST'])
def query():
    data = request.get_json()
    provider = data.get('provider')  # 'openai' or 'gemini'
    prompt = data.get('prompt')
    model = data.get('model')
    response_format = data.get('response_params', {})
    if not provider or not prompt:
        return jsonify({'error': 'Provider and prompt are required'}), 400

    function_params = {
        'prompt_input': prompt,
    }

    if model:
        function_params['model'] = model
    if response_format:
        function_params['response_format'] = response_format
    
    if provider == 'openai':
        response = gpt.api_call_openai(**function_params)
    elif provider == 'gemini':
        response = gem.api_call_gemini(prompt)
    else:
        return jsonify({'error': 'Invalid provider'}), 400

    return jsonify({'response': response})
