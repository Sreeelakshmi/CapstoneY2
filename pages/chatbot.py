import os
from google import genai
from google.genai import types


class NorthEastTravelAdvisorAI:
    def __init__(self, api_key=None, model="gemini-2.0-flash"):
        self.api_key = api_key or os.environ.get("GOOGLE_API_KEY")
        if not self.api_key:
            raise ValueError("API key is required. Set GOOGLE_API_KEY environment variable or pass it directly.")

        self.client = genai.Client(api_key=self.api_key)
        self.model = model

    def generate_travel_advice(self, user_input, conversation_history=None):
        """
        Generates North-East India specific travel advice based on user input and optional conversation history.

        :param user_input: The current query from the user.
        :param conversation_history: Optional chat history (list of past messages for continuity).
        :return: Response from Gemini (North-East focused).
        """
        # Instruction to restrict focus to North-East India
        system_instruction = (
            "You are a travel advisor specialized in destinations, experiences, food, culture, and itineraries "
            "from the North-East region of India, including the states: Arunachal Pradesh, Assam, Manipur, Meghalaya, Mizoram, "
            "Nagaland, Sikkim, and Tripura. Only suggest locations, tips, festivals, and activities related to these states."
        )

        # Initialize conversation history if not provided
        contents = conversation_history or [
            types.Content(role="system", parts=[types.Part.from_text(system_instruction)]),
            types.Content(role="user", parts=[types.Part.from_text("Hi")]),
            types.Content(role="model", parts=[types.Part.from_text("Hello! I'm your North-East India Travel Advisor. How can I assist you today?")])
        ]

        # Append the new user query
        contents.append(
            types.Content(role="user", parts=[types.Part.from_text(user_input)])
        )

        generate_content_config = types.GenerateContentConfig(
            temperature=0.7,
            top_p=0.9,
            top_k=40,
            max_output_tokens=8192,
            response_mime_type="text/plain",
        )

        response = ""
        for chunk in self.client.models.generate_content_stream(
            model=self.model,
            contents=contents,
            config=generate_content_config,
        ):
            response += chunk.text

        return response


# Example Usage
if __name__ == "__main__":
    advisor = NorthEastTravelAdvisorAI(api_key="AIzaSyDNwIxW9HofySRWVYeAjkXTA5by_5LF-j0")  # Replace or set env var
    user_query = "Can you suggest a 7-day itinerary for Meghalaya with budget-friendly homestays?"

    response = advisor.generate_travel_advice(user_query)
    print(response)
