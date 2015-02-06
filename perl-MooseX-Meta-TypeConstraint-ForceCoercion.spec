%define upstream_name    MooseX-Meta-TypeConstraint-ForceCoercion
%define upstream_version 0.01

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

License:	GPL+ or Artistic
Group:		Development/Perl
Summary:	Force coercion when validating type constraints
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/MooseX/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Moose)
BuildRequires:	perl(namespace::autoclean)
BuildRequires:	perl(namespace::clean)
BuildArch:	noarch

%description
This class allows to wrap any 'Moose::Meta::TypeConstraint' in a way that
will force coercion of the value when checking or validating a value
against it.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes LICENSE README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 0.10.0-2mdv2011.0
+ Revision: 655068
- rebuild for updated spec-helper

* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 0.10.0-1mdv2011.0
+ Revision: 401625
- rebuild using %%perl_convert_version
- fixed license field

* Fri May 15 2009 Jérôme Quelin <jquelin@mandriva.org> 0.01-2mdv2010.0
+ Revision: 375940
- rebuild

* Mon May 04 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.01-1mdv2010.0
+ Revision: 371929
- import perl-MooseX-Meta-TypeConstraint-ForceCoercion


* Mon May 04 2009 cpan2dist 0.01-1mdv
- initial mdv release, generated with cpan2dist

