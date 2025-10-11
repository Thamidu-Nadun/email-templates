import os

default_options = {
    'facebook': {
        "url": 'https://www.facebook.com/sliitmozilla',
        "img": 'https://raw.githubusercontent.com/Thamidu-Nadun/email-templates/refs/heads/main/assets/img/facebook.jpg',
        "alt": 'facebook'
    },
    'instagram': {
        "url": 'https://www.instagram.com/sliitmozilla',
        "img": 'https://raw.githubusercontent.com/Thamidu-Nadun/email-templates/refs/heads/main/assets/img/instagram.jpg',
        "alt": 'instagram'
    },
    'github': {
        "url": 'https://github.com/Mozilla-Campus-Club-of-SLIIT',
        "img": 'https://raw.githubusercontent.com/Thamidu-Nadun/email-templates/refs/heads/main/assets/img/github.jpg',
        "alt": 'github'
    },
    'youtube': {
        "url": 'https://www.youtube.com/@sliitmozilla',
        "img": 'https://raw.githubusercontent.com/Thamidu-Nadun/email-templates/refs/heads/main/assets/img/youtube.jpg',
        "alt": 'youtube'
    },
    'linkedin': {
        "url": 'https://www.linkedin.com/company/sliitmozilla/',
        "img": 'https://raw.githubusercontent.com/Thamidu-Nadun/email-templates/refs/heads/main/assets/img/linkedin.jpg',
        "alt": 'linkedin'
    }
}
def generateSocialMediaFooter():
    """Generates a social media footer HTML snippet based on user input or default values.
    This mainly uses to generate the social media footer for the email templates with social media icons in their github repository.
    
    Goal: Get the images from their repository in the path: assets/img/{social_media}.jpg
    
    Returns: str: An HTML string representing the social media footer.
    
    Author: Thamidu Nadun
    
    Date: 2024-06-20
    """
    options = {}
    github_name = input("Enter your GitHub username: ")
    for key, value in default_options.items():
        
        _url = input(f"Enter your {key} URL (default: {value['url']}): ") or value['url']
        _img = f"https://raw.githubusercontent.com/{github_name}/email-templates/refs/heads/main/assets/img/{key}.jpg"
        _alt = input(f"Enter your {key} alt text (default: {value['alt']}): ") or value['alt']
        
        _opt = input(f"{key} url: {_url}\n{key} img: {_img}\n{key} alt: {_alt}\n")
        
        if not _opt: options[key] = value; continue
        value['url'] = _url
        value['img'] = _img
        value['alt'] = _alt
            
        options[key] = {"url": _url, "img": _img, "alt": _alt}
    
    return  f'''<table style="margin-top:1rem;" cellpadding="0" cellspacing="0" border="0" align="center"><tr><td style="padding:5px;outline:none;text-decoration:none;" align="center"><a href="{options['facebook']['url']}"><img src="https://raw.githubusercontent.com/{github_name}/email-templates/refs/heads/main/assets/img/facebook.jpg" alt="{options['facebook']['alt']}" width="15" height="15" style="color:#ff6600;padding:0 4px"/></a><a href="{options['instagram']['url']}"><img src="https://raw.githubusercontent.com/{github_name}/email-templates/refs/heads/main/assets/img/instagram.jpg" alt="instagram" width="15" height="15" style="color:#ff6600;padding:0 4px"/></a><a href="{options['github']['url']}"><img src="https://raw.githubusercontent.com/{github_name}/email-templates/refs/heads/main/assets/img/github.jpg" alt="{options['github']['alt']}" width="15" height="15" style="color:#ff6600;padding:0 4px"/></a><a href="{options['youtube']['url']}"><img src="https://raw.githubusercontent.com/{github_name}/email-templates/refs/heads/main/assets/img/youtube.jpg" alt="{options['youtube']['alt']}" width="15" height="15" style="color:#ff6600;padding:0 4px"/></a><a href="{options['linkedin']['url']}"><img src="https://raw.githubusercontent.com/{github_name}/email-templates/refs/heads/main/assets/img/linkedin.jpg" alt="{options['linkedin']['alt']}" width="15" height="15" style="color:#ff6600;padding:0 4px"/></a></td></tr></table>'''


if __name__ == "__main__":
    res = generateSocialMediaFooter()
    os.makedirs("out", exist_ok=True)
    with open("out/footer.html", "w") as f:
        f.write(res)
    print("[*] Footer HTML has been written to output.html")
