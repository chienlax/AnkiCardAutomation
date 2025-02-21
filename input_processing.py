import google.generativeai as genai
import os
from api_connect import setup_gemini_api  # Import the function from your api_connect.py

def analyze_ielts_passage(passage_text):
    """
    Analyzes an IELTS reading passage using Gemini API to identify advanced words and good phrasing,
    and generates output in Anki basic card format with detailed vocabulary info (V6).

    Args:
        passage_text: The IELTS reading passage text as a string.

    Returns:
        str: The Anki flashcard formatted output as a string, or None if analysis fails.
    """

    model = setup_gemini_api() # Get the Gemini model from your setup function
    if not model:
        print("Gemini API setup failed in analyze_ielts_passage.")
        return None

    prompt_text = f"""
    Analyze the following IELTS reading passage and identify:
    1. Advanced vocabulary words (suitable for IELTS level), especially C1 and C2 level words.
    2. Good phrasing (idiomatic or well-structured phrases).

    For each identified word or phrase, provide the following detailed information in a consistent, structured format, separated by lines and delimiters as shown in the example below:

    -------
    Words: [The identified word or phrase]
    Pronunciation: (US: [US pronunciation], UK: [UK pronunciation])
    Form: [Part of speech, e.g., adj, adv, n, v, phrase]
    Word Family: (n): [Noun form]: (Meaning if different from main word) / (v): [Verb form]: (Meaning if different) / (adj): [Adjective form]: (Meaning if different) / (adv): [Adverb form]: (Meaning if different) (Provide only relevant forms and meanings)
    English Meaning: [Concise and clear English meaning]
    Vietnamese Meaning: [Concise and accurate Vietnamese meaning]
    Example Sentence: [An example sentence in English showing natural usage]
    -------

    Present each identified word/phrase and its detailed information as a separate block, starting and ending with '-------' delimiter lines, exactly as shown above. List these blocks one after another, separated by blank lines. Be as complete as possible for each section, but if information is not readily available or applicable (e.g., word family for a phrase), indicate with 'N/A'. Be concise and avoid extra introductory or concluding text outside of these formatted blocks.

    Passage:
    {passage_text}
    """

    try:
        response = model.generate_content(prompt_text)
        gemini_output = response.text

        # --- Output for debugging and review ---
        print("\n--- Gemini API Response (Raw) ---")
        print(gemini_output)
        print("--- End of Gemini API Response ---")
        print("\nProcessing Gemini Output and Formatting Anki Cards (V6)...")

        anki_card_output = format_gemini_output_to_anki_v6(gemini_output)
        return anki_card_output

    except Exception as e:
        print(f"Error during Gemini passage analysis (V6): {e}")
        return None


def format_gemini_output_to_anki_v6(gemini_output):
    """
    Formats Gemini output to Anki cards, parsing output based on the detailed prompt (V6).
    Expects output blocks delimited by "-----" and specific labels for detailed vocab info.
    """
    anki_output_string = ""
    blocks = gemini_output.strip().split("-------")  # Split into blocks by "-------"

    if not blocks or len(blocks) < 2: # Expecting at least one block pair (start and end delimiter)
        print("Warning (V6): No valid blocks found in Gemini output, or incomplete block delimiters.")
        return ""

    try:
        # Iterate through blocks, skipping empty blocks and assuming blocks come in pairs due to delimiter split
        for i in range(1, len(blocks), 2): # Start from index 1 to skip potential content before first delimiter, step by 2 to get content blocks
            block_text = blocks[i].strip() # Get content between delimiters
            if not block_text:
                continue

            card_data = {
                "Words": None,
                "Pronunciation": None,
                "Form": None,
                "Word Family": None,
                "English Meaning": None,
                "Vietnamese Meaning": None,
                "Example Sentence": None,
            }
            lines = block_text.strip().split("\n")

            for line in lines:
                line = line.strip()
                if line.startswith("Words:"):
                    card_data["Words"] = line[len("Words:"):].strip()
                elif line.startswith("Pronunciation:"):
                    card_data["Pronunciation"] = line[len("Pronunciation:"):].strip()
                elif line.startswith("Form:"):
                    card_data["Form"] = line[len("Form:"):].strip()
                elif line.startswith("Word Family:"):
                    card_data["Word Family"] = line[len("Word Family:"):].strip()
                elif line.startswith("English Meaning:"):
                    card_data["English Meaning"] = line[len("English Meaning:"):].strip()
                elif line.startswith("Vietnamese Meaning:"):
                    card_data["Vietnamese Meaning"] = line[len("Vietnamese Meaning:"):].strip()
                elif line.startswith("Example Sentence:"):
                    card_data["Example Sentence"] = line[len("Example Sentence:"):].strip()

            if all(value is not None for value in card_data.values()): # Check if all data points are extracted
                words = card_data["Words"]
                pronunciation = card_data["Pronunciation"]
                form = card_data["Form"]
                word_family = card_data["Word Family"]
                english_meaning = card_data["English Meaning"]
                vietnamese_meaning = card_data["Vietnamese Meaning"]
                example_sentence = card_data["Example Sentence"]

                anki_output_string += f"Front: {words}\n"
                anki_output_string += f"Back:\n"
                anki_output_string += f"Pronunciation: {pronunciation}\n"
                anki_output_string += f"Form: {form}\n"
                anki_output_string += f"Word Family: {word_family}\n"
                anki_output_string += f"English Meaning: {english_meaning}\n"
                anki_output_string += f"Vietnamese Meaning: {vietnamese_meaning}\n"
                anki_output_string += f"Example Sentence: {example_sentence}\n"
                anki_output_string += "---\n"
            else:
                print(f"Warning (V6): Incomplete data extracted from block: {block_text[:100]}...")

        return anki_output_string

    except Exception as e:
        print(f"Error formatting Gemini output to Anki cards (V6): {e}")
        return None


if __name__ == "__main__":
    # --- Example IELTS Reading Passage (Replace with your actual passage) ---
    example_passage = """
    Urban farming
    In Paris, urban farmers are trying a soil-free approach to agriculture that uses less space and fewer resources. Could it help cities face the threats to our food supplies?
    On top of a striking new exhibition hall in southern Paris, the world's largest urban rooftop farm has started to bear fruit. Strawberries that are small, intensely flavoured and resplendently red sprout abundantly from large plastic tubes. Peer inside and you see the tubes are completely hollow, the roots of dozens of strawberry plants dangling down inside them. From identical vertical tubes nearby burst row upon row of lettuces; near those are aromatic herbs, such as basil, sage and peppermint. Opposite, in narrow, horizontal trays packed not with soil but with coconut fibre, grow cherry tomatoes, shiny aubergines and brightly coloured chards.

    Pascal Hardy, an engineer and sustainable development consultant, began experimenting with vertical farming and aeroponic growing towers - as the soil-free plastic tubes are known - on his Paris apartment block roof five years ago. The urbarn rooftop space above the exhibition hall is somewhat bigger: 14,000 square metres and almost exactly the size of a couple of football pitches. Already, the team of young urban farmers who tend it have picked, in one day, 3,000 lettuces and 150 punnets of strawberries. When the remaining two thirds of the vast open area are in production, 20 staff will harvest up to 1,000 kg of perhaps 35 different varieties of fruit and vegetables, every day. 'We're not ever, obviously, going to feed the whole city this way,' cautions Hardy. 'In the urban environment you're working with very significant practical constraints, clearly, on what you can do and where. But if enough unused space can be developed like this, there's no reason why you shouldn't eventually target maybe between 5% and 10% of consumption.'

    Perhaps most significantly, however, this is a real-life showcase for the work of Hardy's flourishing urban agriculture consultancy, Agripolis, which is currently fielding enquiries from around the world to design, build and equip a new breed of soil-free inner-city farm. 'The method's advantages are many,' he says. 'First, I don't much like the fact that most of the fruit and vegetables we eat have been treated with something like 17 different pesticides, or that the intensive farming techniques that produced them are such huge generators of greenhouse gases. I don't much like the fact, either, that they've travelled an average of 2,000 refrigerated kilometres to my plate, that their quality is so poor, because the varieties are selected for their capacity to withstand such substantial journeys, or that 80% of the price I pay goes to wholesalers and transport companies, not the producers.'

    Produce grown using this soil-free method, on the other hand - which relies solely on a small quantity of water, enriched with organic nutrients, pumped around a closed circuit of pipes, towers and trays - is 'produced up here, and sold locally, just down there. It barely travels at all,' Hardy says. 'You can select crop varieties for their flavour, not their resistance to the transport and storage chain, and you can pick them when they're really at their best, and not before.' No soil is exhausted, and the water that gently showers the plants' roots every 12 minutes is recycled, so the method uses 90% less water than a classic intensive farm for the same yield.

    Urban farming is not, of course, a new phenomenon. Inner-city agriculture is booming from Shanghai to Detroit and Tokyo to Bangkok. Strawberries are being grown in disused shipping containers, mushrooms in underground carparks. Aeroponic farming, he says, is 'virtuous'. The equipment weighs little, can be installed on almost any flat surface and is cheap to buy: roughly €100 to €150 per square metre. It is cheap to run, too, consuming a tiny fraction of the electricity used by some techniques.

    Produce grown this way typically sells at prices that, while generally higher than those of classic intensive agriculture, are lower than soil-based organic growers. There are limits to what farmers can grow this way, of course, and much of the produce is suited to the summer months. 'Root vegetables we cannot do, at least not yet,' he says. 'Radishes are OK, but carrots, potatoes, that kind of thing - the roots are simply too long. Fruit trees are obviously not an option. And beans tend to take up a lot of space for not much return.' Nevertheless, urban farming of the kind being practised in Paris is one part of a bigger and fast-changing picture that is bringing food production closer to our lives.
    """

    print("Analyzing IELTS Passage with Gemini...")
    anki_cards = analyze_ielts_passage(example_passage)

    if anki_cards:
        output_file = "anki_cards_output.txt"
        with open(output_file, "w+", encoding="utf-8") as f:
            f.write(anki_cards)
        print(f"\nAnki flashcards formatted output saved to: {output_file}")
    else:
        print("\nPassage analysis and Anki card generation failed.")