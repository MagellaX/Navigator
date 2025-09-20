<h1 align="center">Navigator Framework</h1>

<p align="center">
  <strong>A framework to enable multimodal models to operate a computer.</strong>
</p>
<p align="center">
  Using the same inputs and outputs as a human operator, the model views the screen and decides on a series of mouse and keyboard actions to reach an objective...
</p>

<!-- Image placeholder: Update with new demo gif -->

## Key Features
- **Compatibility**: Designed for various multimodal models.
- **Integration**: Currently integrated with **GPT-4o, GPT-4.1, o1, Gemini Pro Vision, Claude 3, Qwen-VL and LLaVa.**
- **Future Plans**: Support for additional models.

## Run `Navigator`

1. **Install the project**
```
pip install navigator
```
2. **Run the project**
```
operate
```
3. **Enter your OpenAI Key**: If you don't have one, obtain from [platform.openai.com](https://platform.openai.com/account/api-keys). Edit `.env` for changes.

4. **Permissions**: Grant Terminal "Screen Recording" & "Accessibility" in System Preferences (Mac).

## Using `operate` Modes

#### OpenAI models
Default: gpt-4o (`operate`). For o1: `operate -m o1-with-ocr`. For gpt-4.1: `operate -m gpt-4.1-with-ocr`.

### Multimodal Models `-m`
Gemini: `operate -m gemini-pro-vision` (prompt for Google AI key from [makersuite.google.com](https://makersuite.google.com/app/apikey)).

Claude: `operate -m claude-3` (key from [console.anthropic.com](https://console.anthropic.com/dashboard)).

Qwen: `operate -m qwen-vl` (key from [bailian.console.aliyun.com](https://bailian.console.aliyun.com/)).

LLaVA (Ollama): `operate -m llava` (local; install from [ollama.ai](https://ollama.ai)).

### Voice Mode `--voice`
Clone: `git clone https://github.com/yourorg/navigator.git`  
`cd navigator`  
`pip install -r requirements-audio.txt`  
Mac: `brew install portaudio` | Linux: `sudo apt install portaudio19-dev python3-pyaudio`  
Run: `operate --voice`

### OCR Mode `-m gpt-4-with-ocr`
Default; uses EasyOCR for text-based clicks.

### SoM Mode `-m gpt-4-with-som`
Uses YOLOv8 (`best.pt`) for button detection.

## Contributions
See [CONTRIBUTING.md](CONTRIBUTING.md).

## Feedback
Reach out on Twitter...

## Compatibility
MacOS, Windows, Linux (with an X server installed).

## OpenAI Note
Spend $5+ or more for gpt-4o access: [docs](https://platform.openai.com/docs/guides/rate-limits).
