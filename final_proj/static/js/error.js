const handleError = (error /* string */) => {
    M.toast({
        html: error
    });
    console.error(error);
}