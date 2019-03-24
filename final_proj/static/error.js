const handleError = (error) => {
    M.toast({
        html: error
    });
    console.error(error);
}