import os

default_options = {
    'facebook': {
        "url": 'https://www.facebook.com/sliitmozilla',
        "img": 'https://thamidu-nadun.github.io/email-templates/assets/img/facebook.jpg',
        "alt": 'facebook'
    },
    'instagram': {
        "url": 'https://www.instagram.com/sliitmozilla',
        "img": 'https://thamidu-nadun.github.io/email-templates/assets/img/instagram.jpg',
        "alt": 'instagram'
    },
    'github': {
        "url": 'https://github.com/Mozilla-Campus-Club-of-SLIIT',
        "img": 'https://thamidu-nadun.github.io/email-templates/assets/img/github.jpg',
        "alt": 'github'
    },
    'youtube': {
        "url": 'https://www.youtube.com/@sliitmozilla',
        "img": 'https://thamidu-nadun.github.io/email-templates/assets/img/youtube.jpg',
        "alt": 'youtube'
    },
    'linkedin': {
        "url": 'https://www.linkedin.com/company/sliitmozilla/',
        "img": 'https://thamidu-nadun.github.io/email-templates/assets/img/linkedin.jpg',
        "alt": 'linkedin'
    }
}

def generateSocialMediaFooter():
    """Generates a social media footer HTML snippet based on user input or default values.
    This is used to generate the social media footer for email templates
    with social media icons stored in a GitHub Pages-hosted repository.

    Goal: Get the images from the path:
        https://<github_username>.github.io/email-templates/assets/img/{social_media}.jpg

    Returns:
        str: An HTML string representing the social media footer.

    Author: Thamidu Nadun
    Date: 2024-06-20
    """
    options = {}
    github_name = input("Enter your GitHub username: ")

    for key, value in default_options.items():
        _url = input(f"Enter your {key} URL (default: {value['url']}): ") or value['url']
        _img = f"https://{github_name}.github.io/email-templates/assets/img/{key}.jpg"
        _alt = input(f"Enter your {key} alt text (default: {value['alt']}): ") or value['alt']

        _opt = input(f"{key} url: {_url}\n{key} img: {_img}\n{key} alt: {_alt}\nPress Enter to accept or type 'edit' to modify: ")
        
        if not _opt:
            options[key] = value
            continue

        options[key] = {"url": _url, "img": _img, "alt": _alt}

    # Build HTML
    html = '<table style="margin-top:1rem;" cellpadding="0" cellspacing="0" border="0" align="center"><tr><td style="padding:5px;outline:none;text-decoration:none;" align="center">'
    for key in options:
        html += f'<a href="{options[key]["url"]}"><img src="{options[key]["img"]}" alt="{options[key]["alt"]}" width="15" height="15" style="color:#ff6600;padding:0 4px"/></a>'
    html += '</td></tr></table>'

    return html


if __name__ == "__main__":
    res = generateSocialMediaFooter()
    os.makedirs("out", exist_ok=True)
    output_path = "out/footer.html"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(res)
    print(f"[*] Footer HTML has been written to {output_path}")
