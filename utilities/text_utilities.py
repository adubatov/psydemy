def crop_text(text:str, length:int) -> str: 
    """Crops input text with length more then <length> and add '...' at the end
    """
    postfix = ''
    if len(text) > length:
        postfix = '...'

    return f'{text[:length]}{postfix}'