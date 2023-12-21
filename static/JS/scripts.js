const profilePicture_btn=document.querySelector('.profile-btn');
const dropdown=document.querySelector('.dropdown')
profilePicture_btn.addEventListener('click',()=>{
    if(dropdown.style.visibility=="hidden"){
        dropdown.style.visibility="visible";
    }
    else{
        dropdown.style.visibility="hidden";
    }
});
const OpenModal=document.querySelector('.Open-Modal');
const CloseModal=document.querySelector('.Close-modal');
const modal=document.querySelector('.modal');
OpenModal.addEventListener('click',()=>{
    modal.showModal();
})
CloseModal.addEventListener('click',()=>{
    modal.close();
})

const OpnerEditModal=document.querySelector('.Open-Edit-modal');
const CloseEditModal=document.querySelector('.close-btn');
const EditModal=document.querySelector('.Edit-profile-dialog');
OpnerEditModal.addEventListener('click',()=>{
    EditModal.showModal();
})
CloseEditModal.addEventListener('click',()=>{
    EditModal.close();
})
const OpenpostModal=document.querySelector('.open-post-modal');
const ClosePostMOdal=document.querySelector('close-post-modal');
const PostMOdal=document.querySelector('.Create-post-dialog');
OpenpostModal.addEventListener('click',()=>{
    PostMOdal.showModal();
})
ClosePostMOdal.addEventListener('click',()=>{
    PostMOdal.close();
})